"""Common constants and class to all linters."""

import re
import subprocess
from functools import total_ordering

DEFAULT_MESSAGE_FORMAT = "%(path)s:%(row)d:%(col)d: %(code)s %(text)s"


# TODO use dataclass
@total_ordering
class LinterMessage:
    """Generic linter message."""

    def __init__(
        self,
        tool="unknown",
        message_id="unknown",
        filename="unknown",
        lineno=1,
        charno=1,
        message="unknown",
        extramessage="",
    ):
        """Initializer."""
        self.tool = tool
        self.message_id = message_id
        self.filename = filename
        self.lineno = lineno
        self.charno = charno
        self.message = message
        self.extramessage = extramessage

    def __repr__(self):
        """Represent as a string."""
        return self.formatted(DEFAULT_MESSAGE_FORMAT)

    def as_tuple(self):
        """Represent as a tuple for identification."""
        return (
            self.filename,
            self.lineno,
            self.charno,
            self.message_id,
            self.message,
            self.message_id,
        )

    def __lt__(self, other):
        """Test less than."""
        return self.as_tuple() < other.as_tuple()

    def __eq__(self, other):
        """Test equality."""
        return self.as_tuple() == other.as_tuple()

    def __hash__(self):
        """Compute hash."""
        return hash(self.as_tuple())

    def formatted(self, format_string):
        """Format the message according to format parameter."""
        data = {
            "path": self.filename,
            "row": self.lineno if self.lineno else 1,
            "col": self.charno,
            # horrible hack for visual studio code
            "code": f"W{self.message_id[1:]}",
            "text": f"[{self.tool}] {self.message}",
        }
        if self.extramessage:
            data["text"] += f" ({self.extramessage})"

        return format_string % data


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
    regex = [".*"]

    @classmethod
    def lint(cls, filepath):
        """Execute the linter and return the list of messages."""
        try:
            return cls._lint(filepath)
        except LinterNotFound:
            return [
                LinterMessage(
                    tool="whatalinter",
                    message_id=f"E999",
                    filename=str(filepath),
                    lineno=1,
                    charno=1,
                    message=f"linter not found: {cls.path}",
                    extramessage="",
                )
            ]

    @classmethod
    def _lint(cls, filepath):
        args = [cls.path, str(filepath)]
        result = cls._execute_command(args)
        return cls._parse_output(result.stdout)

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

    @classmethod
    def _parse_line(cls, line, regex, message=None, **kwargs):
        match = re.match(regex, line)
        if match:
            if not message:
                message = LinterMessage()
            kwargs.update(match.groupdict())
            if "lineno" in kwargs:
                kwargs["lineno"] = int(kwargs["lineno"])
            if "charno" in kwargs:
                kwargs["charno"] = int(kwargs["charno"])
            for param, value in kwargs.items():
                setattr(message, param, value)
        else:
            print("ERROR parsing", line)
        return message

    @classmethod
    def _parse_output(cls, output):
        messages = []
        message = ""
        regex_index = 0
        for line in output.splitlines():
            if regex_index == 0:
                message = cls._parse_line(
                    line, cls.regex[regex_index], None, tool=cls.name
                )
            else:
                message = cls._parse_line(
                    line, cls.regex[regex_index], message
                )

            if regex_index == len(cls.regex) - 1:
                regex_index = 0
                messages.append(message)
            else:
                regex_index += 1
        return messages
