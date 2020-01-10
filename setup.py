#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='minnie-config',
    version='0.0.1',
    description='Datajoint configurations for the microns_minnie65_* schemas.',
    author='Christos Papadopoulos',
    author_email='cpapadop@bcm.edu',
    packages=find_packages(exclude=[]),
    install_requires=['datajoint', 'numpy', 'h5py']
)