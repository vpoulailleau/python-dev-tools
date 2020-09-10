"""Linter module, aggregation of linters."""
import argparse
import contextlib
import io
import os
import re
from re import template
import sys
from pathlib import Path
from typing import Union, Optional, List

from flake8.main import application

DEFAULT_MESSAGE_TEMPLATE = "%(path)s:%(row)d:%(col)d: %(code)s %(text)s"


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


def _call_flake8(argv: Optional[List[str]] = None) -> None:
    """Execute the main bit of the application.

    This handles the creation of an instance of :class:`Application`, runs it,
    and then exits the application.

    :param list argv:
        The arguments to be passed to the application for parsing.
    """
    if argv is None:
        argv = sys.argv[1:]

    app = application.Application()
    app.run(argv)
    app.exit()


def _run_flake8(filepath: Path) -> str:
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        try:
            _call_flake8(
                [
                    str(filepath),
                    "--exit-zero",
                    "--max-line-length",
                    "88",
                    "--max-complexity",
                    "10",
                    "--inline-quotes",
                    '"',
                    # E203: space around : in slice
                    # WPS305: avoid f-strings
                    # WPS306: required explicit subclassing of object
                    # WPS602: avoid @staticmethod (can be subclassed…)
                    "--ignore=E203,WPS305,WPS306,WPS602",
                ],
            )
        except SystemExit:
            # TODO what do we do here?
            pass

    return stdout.getvalue()


def _filter_out(message: str) -> bool:
    """Return True when message should be ignored."""
    for authorized_function in ("input", "print", "pprint"):
        if f"Found wrong function call: {authorized_function}" in message:
            return True
    return False


def _add_info(message: str) -> str:
    # TODO
    return message


def _format(message: str, template: str) -> str:
    regex = r"(?P<path>.*?):(?P<row>\d+):(?P<col>\d+):\s+(?P<code>.*?)\s+(?P<text>.*)"
    match = re.match(regex, message)
    if match:
        infos = match.groupdict()
        infos["row"] = int(infos["row"])
        infos["col"] = int(infos["col"])
        message = template % infos
    else:
        print("ERROR parsing:", message)
    return message


def _lint_file(filepath: Path, template: str) -> None:
    flake8_result = _run_flake8(filepath)
    for message in flake8_result.splitlines():
        if _filter_out(message):
            continue
        message = _add_info(message)
        print(_format(message, template))


def lint(path: Union[str, Path], template: str) -> None:
    path = Path(path)
    if path.is_dir():
        for filepath in sorted(path.rglob("*.py")):
            _lint_file(filepath, template)
    else:
        _lint_file(path, template)


def main():
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Python linter combining existing linters",
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        type=str,
        help="path of the file or directory to lint",
    )
    parser.add_argument(
        "-f",
        "--format",
        default=DEFAULT_MESSAGE_TEMPLATE,
        help="format of the output",
    )
    args = parser.parse_args()

    udpate_os_path()
    lint(path=args.path, template=args.format)


if __name__ == "__main__":
    main()
