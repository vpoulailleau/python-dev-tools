"""Pydocstyle linter management."""
import re

from python_dev_tools.linters.common import Linter, LinterMessage


class PydocstyleLinter(Linter):
    """Pydocstyle linter management."""

    name = "pydocstyle"
    path = "pydocstyle"

    @classmethod
    def _lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        header = True
        for line in result.stdout.splitlines():
            if header:
                m = re.match(
                    r"(?P<filename>.*?):(?P<lineno>\d+)\s+"
                    r"(?P<location>.*):",
                    line,
                )
                if m:
                    filename = m.group("filename")
                    lineno = int(m.group("lineno"))
                    location = m.group("location")
                else:
                    print("ERROR parsing", line)
            else:
                m = re.search(r"(?P<message_id>D\d+):\s+(?P<message>.*)", line)
                if m:
                    messages.append(
                        LinterMessage(
                            tool=cls.name,
                            message_id=m.group("message_id"),
                            filename=filename,
                            lineno=lineno,
                            charno=1,
                            message=m.group("message"),
                            extramessage=location,
                        )
                    )
                else:
                    print("ERROR parsing", line)

            header = not header  # message is on two lines
        return messages
