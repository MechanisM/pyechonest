#!/usr/bin/env python
# encoding: utf-8

__version__ = "$Revision: 4.1 $"
# $Source$
from sys import version
from distutils.core import setup

if version < '2.6':
    requires=['urllib', 'urllib2', 'simplejson']
elif version >= '2.6':
    requires=['urllib', 'urllib2', 'json']
else:
    #unknown version?
    requires=['urllib', 'urllib2']

setup(name='beta_pyechonest',
      version='4.0',
      description='Python interface to The Echo Nest APIs.',
      author='Tyler Williams',
      author_email='tyler@echonest.com',
      maintainer='Tyler Williams',
      maintainer_email='tyler@echonest.com',
      url='http://code.google.com/p/pyechonest/',
      download_url='http://code.google.com/p/pyechonest/',
      package_dir={'beta_pyechonest':'pyechonest'},
      packages=['beta_pyechonest'],
      requires=requires
     )
