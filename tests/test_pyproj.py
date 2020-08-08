# flake8: noqa
from pathlib import Path
import re
from os import path

try:
    from pypmeasy import __version__, SyncVersion
except ImportError:
    import sys

    sys.path.insert(0, str(path.dirname(path.dirname(path.abspath(__file__)))))
    try:
        from pypmeasy.pypmeasy import __version__, SyncVersion
    except ImportError:
        sys.path.insert(0, str(path.dirname(path.abspath(__file__))))
        try:
            from pypmeasy import __version__, SyncVersion
        except ImportError:
            from ..pypmeasy import __version__, SyncVersion


class TestClass(object):
    def test_version(self):
        assert __version__ == "0.1.0"

    def test_sync_version(self):
        return SyncVersion.find_version_files(
            str(path.dirname(path.dirname(path.abspath(__file__))))
        )


print(list(map(str, TestClass().test_sync_version())))
