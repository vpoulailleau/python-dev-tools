"""Flake8 linter management."""
import contextlib
import io

from flake8.main.cli import main

from .common import Linter


class Flake8Linter(Linter):
    """Pycodestyle linter management."""

    name = "flake8"
    path = "flake8"
    regex = [
        r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
        r"\s+(?P<message_id>.*?)\s+(?P<message>.*)"
    ]

    @classmethod
    def _lint(cls, filepath):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            main([cls.path, str(filepath), "--exit-zero"])
        messages = cls._parse_output(stdout.getvalue())
        return messages
