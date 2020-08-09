# flake8: noqa
from pathlib import Path
import re
from os import path

try:
    from pyjim import __version__, SyncVersion
except ImportError:
    import sys

    sys.path.insert(0, str(path.dirname(path.dirname(path.abspath(__file__)))))
    try:
        from pyjim.pyjim import __version__, SyncVersion
    except ImportError:
        sys.path.insert(0, str(path.dirname(path.abspath(__file__))))
        try:
            from pyjim import __version__, SyncVersion
        except ImportError:
            from ..pyjim import __version__, SyncVersion


class TestClass(object):
    def test_sync_version_functional(self):
        SyncVersion.find_version_files(
            str(path.dirname(path.dirname(path.abspath(__file__))))
        )
