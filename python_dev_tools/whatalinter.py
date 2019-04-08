"""Linter module, aggregation of linters."""
import argparse
import os
import pathlib

from .linters.common import DEFAULT_MESSAGE_FORMAT
from .linters.lint import lint


def udpate_os_path():
    """Update PATH env variable to find linters."""
    script_path = pathlib.Path(__file__).resolve()
    os.environ["PATH"] = "".join(
        (str(script_path.parent), os.pathsep, os.environ["PATH"])
    )

    # replace /lib/ with /bin/, and add to PATH
    for parent in reversed(script_path.parents):
        if parent.stem == "lib":
            os.environ["PATH"] = "".join(
                (str(parent.parent / "bin"), os.pathsep, os.environ["PATH"])
            )


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Python linter combining existing linters"
    )
    parser.add_argument(
        "file", metavar="FILE", type=str, help="path of the file to lint"
    )
    parser.add_argument(
        "-f",
        "--format",
        default=DEFAULT_MESSAGE_FORMAT,
        help="format of the output",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        default=False,
        help="Display all warnings (default: display first ten warnings)",
    )
    args = parser.parse_args()

    udpate_os_path()
    for message in lint(filepath=args.file, all_warnings=args.all):
        print(message.formatted(args.format))


if __name__ == "__main__":
    main()
