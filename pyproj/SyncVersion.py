from pathlib import Path
import blessings
import os
from typing import List
import re

# import glob


def find_version_files(root_dir: str) -> List[Path]:
    """This function will find the __init__.py(s) in a nontest directory.

    :param str root_dir: Description of parameter `root_dir`.
    :return: Description of returned object.
    :rtype: List[Path]

    """
    root_dir = str(root_dir) if not isinstance(root_dir, str) else root_dir
    rd = Path(root_dir).expanduser()
    try:
        assert rd.exists() and rd.is_dir()
    except AssertionError:
        raise ValueError(
            "Root directory is invalid: it either does not exist or is not a directory"
        )
    version_files = []

    def f():
        with os.scandir(str(rd)) as scan_rd:
            for entry in scan_rd:
                if not entry.name.startswith(".") and entry.is_dir():
                    if entry.name.lower().strip("1234567890!@#$%^&*()_+-=") == "tests":
                        continue

    with os.scandir(str(rd)) as scan_rd:
        for entry in scan_rd:
            if not entry.name.startswith(".") and entry.is_dir():
                if entry.name.lower().strip("1234567890!@#$%^&*()_+-=") == "tests":
                    continue
                else:
                    with os.scandir(entry) as inner_dir:
                        for myentry in inner_dir:
                            if myentry.name == "__init__.py" and myentry.is_file():
                                version_files.append(Path(Path(entry) / Path(myentry)))
    return version_files


def change_version(version_to_change_to: str, contents: str) -> str:
    match = re.search(
        r"(.|\s)*(__version__\s*=\s*)(.*)(.|\s)*", contents, flags=re.IGNORECASE
    )
    if match:
        return match.group(1) + match.group(2) + version_to_change_to + match.group(3)
    else:
        raise ValueError(
            "Could not find __version__ variable.\n\nFile contents:\n{}".format(
                contents
            )
        )


def SyncVersion(version: str, root_dir: str) -> None:
    for file in find_version_files(root_dir):
        file.write_text(change_version(version, file.read_text()))
