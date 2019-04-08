"""McCabe linter management."""
import contextlib
import io

import mccabe

from .common import Linter


class MccabeLinter(Linter):
    """McCabe linter management."""

    name = "McCabe"
    max_complexity = 10
    regex = [r"(?P<lineno>\d+):(?P<charno>\d+):\s+(?P<message>.*)"]

    @classmethod
    def _lint(cls, filepath):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            mccabe.main(["--min", str(cls.max_complexity), str(filepath)])
        messages = cls._parse_output(stdout.getvalue())

        for message in messages:
            message.filename = str(filepath)
            message.message_id = "C901"
            message.message = f"too complex: {message.message}"

        return messages
