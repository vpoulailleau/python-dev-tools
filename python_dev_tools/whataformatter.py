"""Formatter module, aggregation of formatters."""
import argparse
import os
import pathlib

from .formatters.format_file import format_file


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
        description="Python formatter combining existing formatters"
    )
    parser.add_argument(
        "file", metavar="FILE", type=str, help="path of the file to format"
    )
    args = parser.parse_args()

    udpate_os_path()
    format_file(filepath=args.file)


if __name__ == "__main__":
    main()
