from __future__ import absolute_import
from setuptools import setup, find_packages
import os


setup(
    name='nr',
    description='Numerical Recipes',
    author='Andres Quezada Reed',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='test'
)
