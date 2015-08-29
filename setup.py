#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pip
import re
from pip.req import parse_requirements
from setuptools import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


packages = [
    "the_big_username_blacklist"
]

# Handle requirements
requires = parse_requirements("requirements/install.txt",
                              session=pip.download.PipSession())
install_requires = [str(ir.req) for ir in requires]

requires = parse_requirements("requirements/tests.txt",
                              session=pip.download.PipSession())
tests_requires = [str(ir.req) for ir in requires]

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except:
    long_description = ""


version = ''
with open('the_big_username_blacklist/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name="the_big_username_blacklist",
    version=version,
    description="Validate usernames against a blacklist",  # NOQA
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/the-big-username-blacklist-python",
    packages=packages,
    package_data={"": ["LICENSE", ], "the_big_username_blacklist": ["*.txt"]},
    package_dir={"the_big_username_blacklist": "the_big_username_blacklist"},
    include_package_data=True,
    install_requires=install_requires,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy"
    ),
)
