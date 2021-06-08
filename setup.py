# coding: utf-8

"""
    Fabric Orchestrator API

    This is Fabric Orchestrator API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301
from fabric_cf import __VERSION__

NAME = "fabric-orchestrator-client"
VERSION = __VERSION__
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Fabric Orchestrator API",
    author_email="kthare10@unc.edu",
    url="https://github.com/fabric-testbed/OrchestratorClient",
    keywords=["Swagger", "Fabric Orchestrator API"],
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
