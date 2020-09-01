"""Flake8 linter management."""
import contextlib
import io

from flake8.main.cli import main

from python_dev_tools.linters.common import Linter


class Flake8Linter(Linter):
    """Pycodestyle linter management."""

    name = "flake8"
    path = "flake8"
    regex = [
        (
            r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
            + r"\s+(?P<message_id>.*?)\s+(?P<message>.*)"
        ),
    ]

    @classmethod
    def _lint(cls, filepath):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                main(
                    [
                        str(filepath),
                        "--exit-zero",
                        "--max-line-length",
                        "88",
                        "--max-complexity",
                        "10",
                        # Q000: avoid "" strings
                        # WPS305: avoid f-strings
                        # WPS306: required explicit subclassing of object
                        "--ignore=Q000,WPS305,WPS306",
                    ],
                )
            except SystemExit:
                # TODO what do we do here?
                pass

        return cls._parse_output(stdout.getvalue())

    # TODO allow to call "print": https://wemake-python-stylegui.de/en/latest/pages/usage/violations/best_practices.html#wemake_python_styleguide.violations.best_practices.WrongFunctionCallViolation
