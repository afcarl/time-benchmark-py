# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]

setup( 
        name='time_benchmark',
        version='0.1.0',
        description='Time Benchmark',
        long_description = 'See homepage for usage',
        author='Patrick Ng',
        author_email='pn.appdev@gmail.com',
        url='https://github.com/pnpnpn/time-benchmark-py',
        packages=['time_benchmark'],
        install_requires=[],
        #test_suite='tests',
        classifiers=CLASSIFIERS)


