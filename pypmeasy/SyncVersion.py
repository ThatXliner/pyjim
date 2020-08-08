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


def find_version_files(
    root_dir: str, dont_search_dir_names: set = {"tests", "test"}
) -> list:
    """You can use this.

    This function will recursively find the __init__.py(s) in a nontest directory.

    :param str root_dir: Description of parameter `root_dir`.
    :return: Description of returned object.
    :rtype: List[Path]

    """
    root_dir = (
        Path(str(root_dir)).expanduser()
        if not isinstance(root_dir, str)
        else Path(root_dir).expanduser()
    )
    dont_search_dir_names = (
        set(dont_search_dir_names)
        if not isinstance(dont_search_dir_names, set)
        else dont_search_dir_names
    )

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
                    or entry.name.lower().strip("1234567890!@#$%^&*()_+-=") in dsdn
                ):
                    version_files.extend(recursive_find(entry.path, dsdn))
                elif entry.name == "__init__.py" and entry.is_file():
                    version_files.append(Path(entry.path))
        return version_files

    return recursive_find(root_dir, dont_search_dir_names)


def assignment_change_version(
    version_to_change_to: str, contents: str
) -> str:  # noqa D103
    version_to_change_to = (
        str(version_to_change_to)
        if not isinstance(version_to_change_to, str)
        else version_to_change_to
    )
    match = re.search(
        r"(.|\s)*(__version__\s*=\s*)(.*)(.|\s)*", contents, flags=re.IGNORECASE
    )
    if match:
        return (
            match.group(1)
            + match.group(2)
            + repr(version_to_change_to)
            + match.group(3)
        )
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
