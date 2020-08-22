#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""To setup."""
from pathlib import Path
from setuptools import setup, find_packages
from pyjim import __version__, __author__

# The directory containing this file
HERE = Path(Path(__file__).parent)

# The text of the README file
README = Path(HERE / "README.md").read_text()
REQUIREMENTS = Path(HERE / "requirements.txt").read_text().split("\n")
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: POSIX",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development",
    "Typing :: Typed",
]
setup(
    name="pyjim",  # Replace with your own username
    version=__version__,
    author=__author__,
    author_email="bryan.hu.2020@gmail.com",
    description="A setup.py-integrated project manager that actually makes life easier.",
    long_description=README,
    long_description_content_type="text/markdown",
    # url="https://github.com/ThatXliner/pyjim",
    project_urls={
        "Source Code": "https://github.com/ThatXliner/pyjim",
        # "Documentation": "https://pyjim.readthedocs.io/en/latest/index.html",
        "Tracker": "https://github.com/ThatXliner/pyjim/issues",
    },
    packages=find_packages(exclude=["tests"], include=["pyjim"]),
    # scripts=["scripts/pyjim"],
    license="MIT",
    classifiers=CLASSIFIERS,
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[line for line in REQUIREMENTS if not line.startswith("#")],
    # keywords="api stackexchange stackoverflow python webscrape webscrap",
    # entry_points={"console_scripts": ["pyjim=pyjim.__main__:main"]},
)
