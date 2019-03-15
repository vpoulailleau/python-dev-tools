"""Common constants and class to all linters."""

import subprocess
from collections import namedtuple

DEFAULT_MESSAGE_FORMAT = "%(path)s:%(row)d:%(col)d: %(code)s %(text)s"

_LinterMessage = namedtuple(
    "_LinterMessage",
    [
        "tool",
        "message_id",
        "filename",
        "lineno",
        "charno",
        "message",
        "extramessage",
    ],
)


class LinterMessage(_LinterMessage):
    """Generic linter message."""

    def __str__(self):
        """Represent as a string."""
        return self.formatted(DEFAULT_MESSAGE_FORMAT)

    def formatted(self, format):
        """Format the message according to format parameter."""
        data = {
            "path": self.filename,
            "row": self.lineno,
            "col": self.charno,
            # horrible hack for visual studio code
            "code": f"W{self.message_id[1:]}",
            "text": f"[{self.tool}] {self.message}",
        }
        if self.extramessage:
            data["text"] += f" ({self.extramessage})"

        return format % data


class LinterNotFound(FileNotFoundError):
    """
    Exception to detect that a linter is not found.

    Note that this doesn't occur, except due to an installation error.
    """

    pass


class Linter:
    """Base linter class."""

    name = "Linter"
    path = "/bin/unknownlinter"

    @classmethod
    def lint(cls, file):
        """Execute the linter and return the list of messages."""
        try:
            return cls._lint(file)
        except LinterNotFound:
            return [
                LinterMessage(
                    tool="whatalinter",
                    message_id=f"E999",
                    filename=str(file),
                    lineno=1,
                    charno=1,
                    message=f"linter not found: {cls.path}",
                    extramessage="",
                )
            ]

    @classmethod
    def _execute_command(cls, args):
        """Execute the linter or raise LinterNotFound."""
        try:
            return subprocess.run(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10,
                encoding="utf-8",
            )
        except FileNotFoundError as e:
            if e.filename == cls.path:
                raise LinterNotFound
            else:
                raise
