#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
"""Install script for this package."""

import os
from setuptools import setup, find_packages


setup(
    name = "vxcli",
    version = "0.0.0",
    author = "Jaroslav Klapálek",
    author_email = "klapajar@fel.cvut.cz",
    description = ("Command line interface for WindRiver Workbench / VxWorks."),
    license = "GPLv3",
    keywords = "cli vxworks workbench",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    #long_description=read('README'),
    install_requires=["setuptools"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
    scripts=['bin/vxcli'],

)
