"""McCabe linter management."""
from python_dev_tools.linters.common import Linter


class MccabeLinter(Linter):
    """McCabe linter management."""

    name = "McCabe"
    max_complexity = 10
    regex = [r"(?P<lineno>\d+):(?P<charno>\d+):\s+(?P<message>.*)"]

    @classmethod
    def _lint(cls, file):
        args = [
            "python",
            "-m",
            "mccabe",
            "--min",
            str(cls.max_complexity),
            str(file),
        ]
        result = cls._execute_command(args)
        messages = cls._parse_output(result.stdout)
        for message in messages:
            message.message_id = "C901"
            message.message = f"too complex: {message.message}"
        return messages
