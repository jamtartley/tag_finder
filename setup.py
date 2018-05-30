#! /usr/bin/env python3
#! -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tag_finder",
    version="0.0.6",
    author="Sam Hartley",
    author_email="sam@deadcentaur.com",
    description="Find lines of source code you have tagged with custom categories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamtartley/tag_finder",
    include_package_data=True,
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "tagf = tag_finder.__main__:main"
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
)