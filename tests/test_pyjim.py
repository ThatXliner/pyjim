# flake8: noqa
from pathlib import Path
import re
from os import path
import pytest

# TODO: Replace all instances of os.path with the more higher level, pathlib.Path
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
    def test_version(self):
        assert __version__ == "0.1.1"

    #     @pytest.mark.parametrize(
    #     'timeline',
    #     ([1, 2, 3], [2, 4, 6], [6, 8, 10]),
    #     indirect=True
    # )
    def test_sync_version(self):
        assert SyncVersion.find_version_files(
            str(path.dirname(path.dirname(path.abspath(__file__))))
        ) == [
            Path(
                path.join(
                    path.join(
                        path.dirname(path.dirname(path.abspath(__file__))), "pyjim"
                    ),
                    "__init__.py",
                )
            )
        ]
