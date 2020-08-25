#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: v0.0.1.1

Desc: A description or summary here

"""

from pathlib import Path
import blessings

import re
import logging
import warnings

NONE_ALPHABET = re.compile(r"[^a-zA-Z]")
FIND_VERSION = re.compile(
    r"(.|\s)*(__version__\s*=\s*)(?:(?<!\\)(\"|'))(.*)(?:(?<!\\)\3)(.|\s)*",
    flags=re.IGNORECASE,
)


def find_version_files(
    root_dir: str, dont_search_dir_names: set = {"tests", "test"}
) -> list:
    """You can use this.

    This function will recursively find the __init__.py(s) in a nontest directory.

    :param str root_dir: Description of parameter `root_dir`.
    :return: Description of returned object.
    :rtype: List[Path]

    """
    root_dir = Path(str(root_dir)).expanduser()
    dont_search_dir_names = set(map(str, dont_search_dir_names))

    try:
        assert root_dir.exists() and root_dir.is_dir()
    except AssertionError:
        raise ValueError(
            "Root directory is invalid: it either does not exist or is not a directory"
        )
    from os import scandir

    def recursive_find(rd, dsdn):
        version_files = []
        rd = Path(str(rd)).expanduser()
        with scandir(str(rd)) as scan_rd:
            for entry in scan_rd:
                if entry.is_dir() and not (
                    entry.name.startswith(".")
                    or NONE_ALPHABET.sub("", entry.name.lower()) in dsdn
                ):
                    version_files.extend(recursive_find(entry.path, dsdn))
                elif entry.name == "__init__.py" and entry.is_file():
                    version_files.append(Path(entry.path))
        return version_files

    return recursive_find(root_dir, dont_search_dir_names)


def assignment_change_version(
    version_to_change_to: str, contents: str
) -> str:  # noqa D103
    version_to_change_to = str(version_to_change_to)
    match = FIND_VERSION.search(contents)
    if match:
        return match.group(2) + repr(version_to_change_to)
    else:
        raise ValueError(
            "Could not find __version__ variable.\n\nFile contents:\n{}".format(
                contents
            )
        )


def SyncVersion(version: str, root_dir: str, log: bool = True) -> None:
    """Short summary.

    :param str version: Description of parameter `version`.
    :param str root_dir: Description of parameter `root_dir`.
    :param bool log: Description of parameter `log`. Defaults to True.
    :return: Description of returned object.
    :rtype: None

    """
    if log:
        print(
            """
            Version detected: setting all
            occurences of assignment of the
            __version__ magic variable to {}
            """.format(
                version
            )
        )
        for file in find_version_files(root_dir):
            print("Attempting to find version version in file: {}".format(file))
            try:
                file.write_text(assignment_change_version(version, file.read_text()))
            except ValueError:
                warnings.warn(
                    "Could not find __version__ magic variable in {} .".format(file)
                )
                continue
            print("Skipping...")
    else:  # We do this because of readability and performance
        for file in find_version_files(root_dir):
            try:
                file.write_text(assignment_change_version(version, file.read_text()))
            except ValueError:
                warnings.warn(
                    "Could not find __version__ magic variable in {} .".format(file)
                )
                continue


def find_version(file):
    """Retrieve the version.

    :param type file: Description of parameter `file`.
    :return: Description of returned object.
    :rtype: type

    """
    if hasattr(file, "read"):
        return FIND_VERSION.search(file.read())[4]
    elif hasattr(file, "read_text"):
        return FIND_VERSION.search(file.read_text())[4]
    elif hasattr(file, "__str__"):
        return FIND_VERSION.search(str(file))[4]
    else:
        return FIND_VERSION.search(file)[4]
    # from io import StringIO, TextIOBase
    #
    # if file is Path:
    #
    #     return FIND_VERSION.search(file.read_text())[4]
    # elif file is StringIO:
    #     ...
    # elif file is TextIOBase:
    #     return FIND_VERSION.search(file)[4]
    # elif file is str:
    #     return FIND_VERSION.search(file)[4]
