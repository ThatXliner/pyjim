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
    """Use this as the entry point.

    The main driver program for pyjim.

    :return: This function doesn't return anything.
    :rtype: None

    """
    # TODO: Explicitly add the dest argument
    # TODO: Explicitly add the usage argument
    import argparse
    import sys
    from pathlib import Path  # noqa
    from json import dumps
    import os

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
        description="A setup.py-integrated project manager that actually makes life "
        "easier.",
        prog="pyjm",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--no-fancy",
        action="store_true",
        help="Don't display fancily. Infers --no-color.",
        default=False,
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Don't display in color.",
        default=False,
    )
    subcommands = parser.add_subparsers(
        description="The main sub-commands to use.", title="Commands", dest="which"
    )
    ####################################################################################
    # VERSION COMMAND ##################################################################
    ####################################################################################
    version_command = subcommands.add_parser(
        "version",
        help="These commands are all related with version manipulation, "
        "version management, and more.",
        aliases=["ver", "v", "vers"],
    )
    version_command_command = version_command.add_subparsers(
        title="Version manipulation commands",
        help="Use these commands to manipulate or view the version of the project you're "
        "using pyjim to manage",
        dest="version_command",
    )
    version_info = version_command_command.add_parser(
        "info",
        help="Display the version information of the project you're "
        "using pyjim to manage",
        aliases=["i", "in", "inf"],
    )
    version_info.add_argument(
        "--raw", action="store_true", default=False, help="Output raw JSON."
    )

    version_set = version_command_command.add_parser(
        "set", help="Set the version of this project.", aliases=["s"]
    )
    version_set.add_argument("version", help="The version to set to.")

    version_pyjim = version_command_command.add_parser(
        "pyjim",
        help="Display the version information of pyjim.",
        aliases=["p", "pjm", "pyjm", "pjym", "pyjym"],
    )
    version_pyjim.add_argument(
        "--major-only", "--m-o", help="Only display the major version of pyjim."
    )

    ####################################################################################
    # INFO COMMAND #####################################################################
    ####################################################################################
    info_command = subcommands.add_parser(
        "info",
        help="If you want general information about your project or about this tool, "
        "use this command.",
        aliases=["i", "information", "inf", "in"],
    )
    info_command_command = info_command.add_subparsers(
        title="Informative commands",
        help="Use these commands to get general information about something.",
        dest="info_command",
    )
    info_version = info_command_command.add_parser(
        "version",
        help="Get information about the version (either from your project or pyjim)",
    )
    info_version.add_argument(
        "type",
        nargs=1,
        help="The type of version get information from",
        choices=["pyjim", "project", "this"],
    )
    ####################################################################################
    # UPLOAD COMMAND ###################################################################
    ####################################################################################
    upload_command = subcommands.add_parser(
        "upload",
        help="This command will upload your project to PyPi or TestPyPi. Depending on "
        "the settings you provide",
        aliases=["up", "u", "upl", "publish", "pub", "p"],
    )
    upload_command.add_argument(
        "--arguments",
        "--args",
        "-a",
        nargs="+",
        action="append",
        default="sdist bdist_wheel",
        help="The arguments to pass to `python setup.py` for building "
        "(which will be ran internally).",
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
        "build", help="This command will build your project, ready for distribution.",
    )
    build_command.add_argument(
        "--arguments",
        "--args",
        "-a",
        nargs="+",
        action="append",
        default="sdist bdist_wheel",
        help="The arguments to go with python setup.py for building.",
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
    ####################################################################################
    # VERSION COMMAND PARSE ############################################################
    ####################################################################################

    if args.which in ["ver", "v", "vers", "version"]:
        # INFO
        PROJECT_VERSION = SyncVersion.find_version_files(
            os.getcwd(), dont_search_dir_names="tests"
        )[0]
        if args.version_command in ["info", "i", "in", "inf"]:
            if args.raw:  # Output raw JSON

                print(
                    dumps(
                        {"pyjim": __version__, "project": PROJECT_VERSION},
                        indent=4,
                        sort_keys=True,
                    )
                )


if __name__ == "__main__":
    print(main())
