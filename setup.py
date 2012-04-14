#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from objectifier import metadata

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='objectifier',
    version=metadata.__version__,
    url='https://github.com/elmcitylabs/objectifier',
    license=metadata.__license__,
    description='Turns dictionaries into Python objects.',
    author=metadata.__author__,
    author_email=metadata.__email__,
    packages=['objectifier'],
    package_data={'': ['LICENSE', 'README']},
)

