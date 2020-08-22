"""Tests."""
from pathlib import Path

import pytest

HERE = Path(Path(__file__).absolute().as_posix())
try:
    from pyjim import __version__, SyncVersion
except ImportError:
    import sys

    sys.path.insert(0, Path(HERE.parent).parent)
    try:
        from pyjim.pyjim import __version__, SyncVersion
    except ImportError:
        try:
            from pyjim import __version__, SyncVersion
        except ImportError:
            sys.path.insert(0, Path(HERE).parent)
            try:
                from pyjim import __version__, SyncVersion
            except ImportError:
                from ..pyjim import __version__, SyncVersion


class TestClass(object):  # noqa
    def test_sync_version(self):  # noqa
        assert SyncVersion.find_version_files(str(Path(Path(HERE).parent).parent)) == [
            Path(Path(Path(Path(Path(HERE).parent).parent) / "pyjim") / "__init__.py")
        ]
