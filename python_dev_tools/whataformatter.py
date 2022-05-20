"""Formatter module, aggregation of formatters."""
import argparse
import difflib
import os
import shutil
from pathlib import Path

from python_dev_tools.formatters.format_file import format_file


def udpate_os_path():
    """Update PATH env variable to find linters."""
    script_path = Path(__file__).resolve()
    os.environ["PATH"] = "".join(
        (str(script_path.parent), os.pathsep, os.environ["PATH"]),
    )

    # replace /lib/ with /bin/, and add to PATH
    for parent in reversed(script_path.parents):
        if parent.stem == "lib":
            os.environ["PATH"] = "".join(
                (str(parent.parent / "bin"), os.pathsep, os.environ["PATH"]),
            )


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Python formatter combining existing formatters",
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        type=str,
        help="path of the file to format",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        default=False,
        help="ignored flag (compatibility with black / VS Code)",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        default=False,
        help="display diff instead of writing file",
    )
    parser.add_argument(
        "--target-version",
        type=str,
        default="py39",
        help="target version for formatting",
    )
    # TODO passer cet argument à black et pyupgrade
    args = parser.parse_args()

    udpate_os_path()
    if args.diff:
        copy_file = f"{args.file}.co.py"
        shutil.copyfile(args.file, copy_file)
        format_file(filepath=copy_file)
        orig_content = Path(args.file).read_text()
        copy_content = Path(copy_file).read_text()
        print(
            "".join(
                difflib.unified_diff(
                    [line + "\n" for line in orig_content.splitlines()],
                    [line + "\n" for line in copy_content.splitlines()],
                    fromfile=args.file,
                    tofile=args.file,
                ),
            ),
        )
        Path(copy_file).unlink()
    else:
        format_file(filepath=args.file)


if __name__ == "__main__":
    main()
