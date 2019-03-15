"""Pyflakes linter management."""
import re

from python_dev_tools.linters.common import Linter, LinterMessage


class PyflakesLinter(Linter):
    """Pyflakes linter management."""

    name = "pyflakes"
    path = "pyflakes"

    @classmethod
    def _lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        for line in result.stdout.splitlines():
            m = re.match(
                r"(?P<filename>.*?):(?P<lineno>\d+):\s+(?P<message>.*)", line
            )
            if m:
                messages.append(
                    LinterMessage(
                        tool=cls.name,
                        message_id="W999",
                        filename=m.group("filename"),
                        lineno=int(m.group("lineno")),
                        charno=1,
                        message=m.group("message"),
                        extramessage="",
                    )
                )
            else:
                print("ERROR parsing", line)

        return messages
