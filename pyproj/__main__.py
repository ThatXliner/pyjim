#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# noqa F401
"""
Author: Bryan Hu .

@Bryan Hu .

Made with love by Bryan Hu .


Version: v0.1.0

Desc: The main script to use.

"""


def main():  # noqa
    import argparse
    import sys
    from os import path

    sys.path.insert(0, "..")
    from pyproj import __version__

    parser = argparse.ArgumentParser(
        description="""A setup.py-integrated project manager that actually makes life
        easier.""",
        prog="pyproj",
        epilog="""We're no hippocrites: poetry was the only thing that was 'good' enough
        at the time""",
        # usage="pyproj [-h] {version, info, upload, build, help} ..."
        # version=__version__,
        # formatter_class=argparse.RawTextHelpFormatter,
    )
    subcommands = parser.add_subparsers(
        description="The commands to use.", dest="subcs", title="Commands",
    )
    version_command = subcommands.add_parser(
        "version",
        help="""
        Use this to interact with the project's version or to interact with anything
        version-related. Version control systems not included (for now).""",
    )
    version_command_commands = version_command.add_subparsers(
        title="Version manipulation commands",
        dest="verc",
        help="Use these commands to manipulate or view the version of this project",
    )
    version_info = version_command_commands.add_parser(
        "info", help="Display the version information."
    )
    version_info.add_argument(
        "--no-fancy",
        action="store_true",
        help="Don't display info fancily. Infers --no-color.",
        default=False,
    )
    version_info.add_argument(
        "--no-color",
        action="store_true",
        help="Don't display info in color.",
        default=False,
    )
    version_info.add_argument(
        "--raw", action="store_true", default=False, help="Output raw JSON."
    )
    version_set = version_command_commands.add_parser(
        "set", help="Set the version of this project."
    )
    version_set.add_argument("version", help="The version to set to.")
    info_command = subcommands.add_parser(
        "info",
        help="""If you want general information about your project or this tool,
 use this command.""",
    )
    upload_command = subcommands.add_parser(
        "upload",
        help="""This command will *print* the
        command to upload your project to PyPi or TestPyPi. It should be used like this:
        pyproj upload | xargs /bin/bash/
    """,
    )
    build_command = subcommands.add_parser(
        "build",
        help="""This command will *print* the command to build your project
        to be ready for distribution.

        It should be used like this: pyproj build | xargs /bin/bash/ """,
    )
    build_command.add_argument(
        "arguments",
        nargs="+",
        default="sdist bdist_wheel",
        help="The arguments to go with python setup.py",
    )
    help_command = subcommands.add_parser(
        "help", help="For getting help about other commands."
    )
    args = parser.parse_args(sys.argv[1:])
    return None


if __name__ == "__main__":
    main()
