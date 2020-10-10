#!/usr/bin/env python3


from setuptools import find_packages, setup

setup(
    author="Codemaze",
    # install_requires=["boto3"],
    license="MIT",
    name="utils",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=["pytest"],
    version="1.0.0"
)
