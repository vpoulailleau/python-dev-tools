"""Pyflakes linter management."""
from python_dev_tools.linters.common import Linter


class PyflakesLinter(Linter):
    """Pyflakes linter management."""

    name = "pyflakes"
    path = "pyflakes"
    regex = [r"(?P<filename>.*?):(?P<lineno>\d+):\s+(?P<message>.*)"]

    @classmethod
    def _lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = cls._parse_output(result.stdout)
        for message in messages:
            message.message_id = "W999"
        return messages
