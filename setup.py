#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""setup.py - Generic setup script."""


import setuptools


setuptools.setup(
    install_requires=[
        "chardet==3.0.4",
        "colorama==0.4.3",
        "docopt==0.6.2",
        "idna==2.8",
        "junit-xml==1.8",
        "lark-parser==0.7.8",
        "python-hcl2==0.2.5",
        "pyyaml==5.2",
        "requests==2.22.0",
        "six==1.13.0",
        "tabulate==0.8.6",
        "termcolor==1.1.0",
        "urllib3==1.25.8",
        "dpath==1.5.0",
    ],
    name="pre-commit",
    description="Rewrite Terraform configuration files to a canonical format"
    "and style",
    url="https://github.com/melmorabity/pre-commit-terraform-fmt",
    version="0.1.3",
    author=["Pingzhou Liu"],
    author_email="applegreengrapeintherain@gmail.com",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(exclude="tests"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-datafiles", "pytest-pylint"],
    entry_points={
        "console_scripts": [
            "myChecks = myChecks.run:run",
        ]
    },
)
