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


def main() -> None:
    """Short summary.

    Long description.

    :return: This function doesn't return anything.
    :rtype: None

    """
    # TODO: Explicitly add the dest argument
    # TODO: Explicitly add the usage argument
    import argparse
    import sys
    from os import path

    # TODO: Replace os.path with pathlib.Path

    # import subprocess
    import shlex

    # from blessings import Terminal

    try:
        from . import __version__
    except ImportError:
        try:
            sys.path.insert(0, "..")
            from pyjim import __version__
        except ImportError:
            try:
                from pyjim import __version__
            except ModuleNotFoundError as e:
                raise e

    try:
        from . import SyncVersion
    except ImportError:
        try:
            import SyncVersion
        except ImportError:
            try:
                from pyjim import SyncVersion
            except ModuleNotFoundError as e:
                raise e
    # t = Terminal()
    parser = argparse.ArgumentParser(
        description="""A setup.py-integrated project manager that actually makes life
        easier.""",
        prog="pyjm",
        epilog="""We're no hippocrites: poetry was the only thing that was 'good' enough
        at the time""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subcommands = parser.add_subparsers(
        description="The commands to use.", title="Commands", dest="which"
    )
    ####################################################################################
    # VERSION COMMAND ##################################################################
    ####################################################################################
    version_command = subcommands.add_parser(
        "version",
        help="""
       Use this to interact with the project's version or to interact with anything
       version-related. Version control systems not included (for now).""",
        aliases=["v", "version"],
    )
    version_command_command = version_command.add_subparsers(
        title="Version manipulation commands",
        help="Use these commands to manipulate or view the version of this project",
        dest="version_command",
    )
    version_info = version_command_command.add_parser(
        "info",
        help="Display the version information of this project.",
        aliases=["ver", "v", "vers"],
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
    version_set = version_command_command.add_parser(
        "set", help="Set the version of this project."
    )
    version_set.add_argument("version", help="The version to set to.")
    version_pyjim = version_command_command.add_parser(  # noqa
        "pyjim",
        help="Display the version information of pyjim.",
        aliases=["ver", "v", "vers"],
    )

    ####################################################################################
    # INFO COMMAND #####################################################################
    ####################################################################################
    info_command = subcommands.add_parser(
        "info",
        help="""If you want general information about your project or this tool,
    use this command.""",
    )
    info_command_command = info_command.add_subparsers(
        title="Informative commands",
        help="Use these commands to get general information about something.",
        dest="info_command",
    )
    info_command_command.add_parser(
        "version",
        help="Get information about the version (either from your project or pyjim)",
    )
    ####################################################################################
    # UPLOAD COMMAND ###################################################################
    ####################################################################################
    upload_command = subcommands.add_parser(
        "upload",
        help="""This command will *print* the
       command to upload your project to PyPi or TestPyPi. It should be used like this:
       pyjim upload | xargs /bin/bash/
    """,
    )
    upload_command.add_argument(
        "build_args",
        nargs="*",
        action="append",
        default="sdist bdist_wheel",
        help="The arguments to pass to `python setup.py` (which will be ran internally)",
    )
    upload_command.add_argument(
        "--print-only",
        "-p",
        action="store_true",
        default=False,
        help="To only print the command instead of executing it.",
    )
    ####################################################################################
    # BUILD COMMAND ####################################################################
    ####################################################################################
    build_command = subcommands.add_parser(
        "build",
        help="""This command will *print* the command to build your project
       to be ready for distribution.

       It should be used like this: pyjim build | xargs /bin/bash/ """,
    )
    build_command.add_argument(
        "arguments",
        nargs="*",
        action="append",
        default="sdist bdist_wheel",
        help="The arguments to go with python setup.py",
    )
    ####################################################################################
    # HELP COMMAND #####################################################################
    ####################################################################################
    help_command = subcommands.add_parser(
        "help", help="For getting help about other commands."
    )
    help_command.add_argument(
        "command",
        help="The command to get help for",
        choices=["help", "info", "build", "version", "upload"],
    )
    args = parser.parse_args(sys.argv[1:])  # noqa
    return args


if __name__ == "__main__":
    print(main())
