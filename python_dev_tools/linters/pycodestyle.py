"""Pycodestyle linter management."""
import re

from python_dev_tools.linters.common import Linter, LinterMessage


class PycodestyleLinter(Linter):
    """Pycodestyle linter management."""

    name = "pycodestyle"
    path = "pycodestyle"

    @classmethod
    def _lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        for line in result.stdout.splitlines():
            m = re.match(
                r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
                r"\s+(?P<message_id>.*?)\s+(?P<message>.*)",
                line,
            )
            if m:
                messages.append(
                    LinterMessage(
                        tool=cls.name,
                        message_id=m.group("message_id"),
                        filename=m.group("filename"),
                        lineno=int(m.group("lineno")),
                        charno=int(m.group("charno")),
                        message=m.group("message"),
                        extramessage="",
                    )
                )
            else:
                print("ERROR parsing", line)

        return messages
