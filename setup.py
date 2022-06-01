#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='MLForEveryone',
    version='1.0.0',
    description='A series of accessible tutorials on learning Machine Learning using the Python programming language!',
    author='Alex Morehead',
    author_email='alex.morehead@gmail.com',
    license='GNU Public License, Version 3.0',
    url='https://github.com/amorehead/MLForEveryone',
    install_requires=[
        'matplotlib',
        'sklearn',
        'ipykernel'
    ],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Education',
        'License :: OSI Approved :: MIT',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ]
)
