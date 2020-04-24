# -*- coding: utf-8 -*-
"""Checkov"""

import argparse
import subprocess
import sys
import os.path
from checkov.cloudformation.runner import Runner as cfn_runner
from checkov.common.runners.runner_registry import RunnerRegistry
from checkov.common.util.docs_generator import print_checks
from checkov.terraform.runner import Runner as tf_runner
from checkov.version import version

def run(filenames):
    """Run 'checkov' command on a dir."""
    myrootfolder = ""
    folders = []
    for files in filenames:
        folders.append(os.path.dirname(files))

    myrootfolder = os.path.join(
        os.path.abspath(min(folders, key=len, default=".")), ""
    )
    print(myrootfolder)


def main(argv=None):
    """Main execution path."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )

    parser.add_argument("-d", help="directory to run against")

    args = parser.parse_args(argv)

    return run(args.filenames)


if __name__ == "__main__":
    exit(main())