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

    # from blessings import Terminal

    try:
        from . import __version__
    except ImportError:
        try:
            sys.path.insert(0, "..")
            from pypmeasy import __version__
        except ImportError:
            try:
                from pypmeasy import __version__
            except ModuleNotFoundError as e:
                raise e

    try:
        from . import SyncVersion
    except ImportError:
        try:
            import SyncVersion
        except ImportError:
            try:
                from pypmeasy import SyncVersion
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
        description="The commands to use.", title="Commands",
    )
    ####################################################################################
    # VERSION COMMAND ##################################################################
    ####################################################################################
    version_command = subcommands.add_parser(
        "version",
        help="""
        Use this to interact with the project's version or to interact with anything
        version-related. Version control systems not included (for now).""",
    )
    version_command_command = version_command.add_subparsers(
        title="Version manipulation commands",
        help="Use these commands to manipulate or view the version of this project",
    )
    version_info = version_command_command.add_parser(
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
    version_set = version_command_command.add_parser(
        "set", help="Set the version of this project."
    )
    version_set.add_argument("version", help="The version to set to.")
    ####################################################################################
    # INFO COMMAND #####################################################################
    ####################################################################################
    info_command = subcommands.add_parser(
        "info",
        help="""If you want general information about your project or this tool,
 use this command.""",
    )
    ####################################################################################
    # UPLOAD COMMAND ###################################################################
    ####################################################################################
    upload_command = subcommands.add_parser(
        "upload",
        help="""This command will *print* the
        command to upload your project to PyPi or TestPyPi. It should be used like this:
        pypmeasy upload | xargs /bin/bash/
    """,
    )
    ####################################################################################
    # BUILD COMMAND ####################################################################
    ####################################################################################
    build_command = subcommands.add_parser(
        "build",
        help="""This command will *print* the command to build your project
        to be ready for distribution.

        It should be used like this: pypmeasy build | xargs /bin/bash/ """,
    )
    build_command.add_argument(
        "arguments",
        nargs="*",
        default="sdist bdist_wheel",
        help="The arguments to go with python setup.py",
    )
    ####################################################################################
    # HELP COMMAND #####################################################################
    ####################################################################################
    help_command = subcommands.add_parser(
        "help", help="For getting help about other commands."
    )
    args = parser.parse_args(sys.argv[1:])  # noqa
    version_args = version_command.parse_args(sys.argv[1:])  # noqa
    info_args = info_command.parse_args(sys.argv[1:])  # noqa
    build_args = build_command.parse_args(sys.argv[1:])  # noqa
    help_args = help_command.parse_args(sys.argv[1:])  # noqa
    upload_args = upload_command.parse_args(sys.argv[1:])  # noqa
    # print("{}{}args:{}".format(t.bold, t.red, t.normal))
    # print(args)
    # print("{}{}version_args:{}".format(t.bold, t.red, t.normal))
    # print(version_args)
    # print("{}{}build_args:{}".format(t.bold, t.red, t.normal))
    # print(build_args)
    # print("{}{}help_args:{}".format(t.bold, t.red, t.normal))
    # print(help_args)
    # print("{}{}upload_args:{}".format(t.bold, t.red, t.normal))
    # print(upload_args)
    # print("{}{}info_args:{}".format(t.bold, t.red, t.normal))
    # print(info_args)
    return None


if __name__ == "__main__":
    main()
