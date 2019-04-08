"""Pyflakes linter management."""
from .common import Linter


class PyflakesLinter(Linter):
    """Pyflakes linter management."""

    name = "pyflakes"
    path = "pyflakes"
    regex = [r"(?P<filename>.*?):(?P<lineno>\d+):\s+(?P<message>.*)"]

    @classmethod
    def _lint(cls, filepath):
        args = [cls.path, str(filepath)]
        result = cls._execute_command(args)
        messages = cls._parse_output(result.stdout)
        for message in messages:
            message.message_id = "W999"
        return messages
