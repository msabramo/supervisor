##############################################################################
#
# Copyright (c) 2006-2013 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
import sys

if sys.version_info[:2] < (2, 5):
    msg = ("Supervisor requires Python 2.5 or later. You are using version %s. "
           "Please install using a supported version." % sys.version)
    sys.stderr.write(msg)
    sys.exit(1)

requires = ['meld3 >= 0.6.5']
tests_require = []
if sys.version_info[:2] < (3, 3):
    tests_require.append('mock')
    
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    README = """\
Supervisor is a client/server system that allows its users to
control a number of processes on UNIX-like operating systems. """
    CHANGES = ''

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
]

version_txt = os.path.join(here, 'supervisor/version.txt')
supervisor_version = open(version_txt).read().strip()

dist = setup(
    name = 'supervisor',
    version = supervisor_version,
    license = 'BSD-derived (http://www.repoze.org/LICENSE.txt)',
    url = 'http://supervisord.org/',
    description = "A system for controlling process state under UNIX",
    long_description=README + '\n\n' +  CHANGES,
    classifiers = CLASSIFIERS,
    author = "Chris McDonough",
    author_email = "chrism@plope.com",
    maintainer = "Mike Naberezny",
    maintainer_email = "mike@naberezny.com",
    packages = find_packages(),
    install_requires = requires,
    extras_require = {'iterparse':['cElementTree >= 1.0.2']},
    tests_require = tests_require,
    include_package_data = True,
    zip_safe = False,
    test_suite = "supervisor.tests",
    entry_points = {
     'console_scripts': [
         'supervisord = supervisor.supervisord:main',
         'supervisorctl = supervisor.supervisorctl:main',
         'echo_supervisord_conf = supervisor.confecho:main',
         'pidproxy = supervisor.pidproxy:main',
        ],
    },
)
