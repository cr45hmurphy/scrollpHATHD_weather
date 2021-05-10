#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(
    name = 'weather', 
    version = '1.0', 
    packages = ['lib']
)
