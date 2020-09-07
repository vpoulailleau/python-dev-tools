"""Flake8 linter management."""
import contextlib
import io

from flake8.main.cli import main

from python_dev_tools.linters.common import Linter, LinterMessage


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

        return cls._parse_output(stdout.getvalue())

    @staticmethod
    def filter_out(message: LinterMessage) -> bool:
        """Return True when message should be ignored."""
        for authorized_function in ("input", "print", "pprint"):
            if f"Found wrong function call: {authorized_function}" in message.message:
                return True
        return False
