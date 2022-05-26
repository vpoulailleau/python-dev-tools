"""Formatter module, aggregation of formatters."""
import argparse
import difflib
import os
import shutil
import subprocess  # noqa: S404
from pathlib import Path
from typing import List, NamedTuple


class FormatterConfig(NamedTuple):
    """Configuration of formatting tool."""

    name: str
    path: str
    cli_args: List[str]


_formatters_configs: List[FormatterConfig] = [
    FormatterConfig(
        name="autoflake",
        path="autoflake",
        cli_args=["--in-place", "--remove-unused-variables"],
    ),
    FormatterConfig(name="pyupgrade", path="pyupgrade", cli_args=["--py37-plus"]),
    FormatterConfig(
        name="black",
        path="black",
        cli_args=["--target-version=py37"],
    ),  # Should be the last config
]


def _format_file(filepath: str, config: FormatterConfig) -> None:
    """Execute the formatter.

    Args:
        filepath (str): path of the file to format
        config (FormatterConfig): configuration for the formatting tool

    Returns:
        None
    """
    try:
        return subprocess.run(  # noqa: S603
            [config.path, *config.cli_args, filepath],
            capture_output=True,
            timeout=10,
            encoding="utf-8",
        )
    except FileNotFoundError as exc:
        if exc.filename == config.path:
            print(f"Formatter {config.name} not found: {config.path}")


def format_file(filepath: str) -> None:
    """Format the file with known formatters.

    Args:
        filepath (str): path of the file to format
    """
    for config in _formatters_configs:
        _format_file(filepath, config)


def udpate_os_path() -> None:
    """Update PATH env variable to find linters."""
    paths = os.environ["PATH"].split(os.pathsep)
    script_path = Path(__file__).resolve()
    paths.insert(0, str(script_path.parent))

    # replace /lib/ with /bin/, and add to PATH
    for parent in reversed(script_path.parents):
        if parent.stem == "lib":
            paths.insert(0, str(parent.parent / "bin"))

    os.environ["PATH"] = os.pathsep.join(paths)


def main() -> None:
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
                    [f"{line}\n" for line in orig_content.splitlines()],
                    [f"{line}\n" for line in copy_content.splitlines()],
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
