"""McCabe linter management."""
import re

from python_dev_tools.linters.common import Linter, LinterMessage


class MccabeLinter(Linter):
    """McCabe linter management."""

    name = "McCabe"
    max_complexity = 10

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
        messages = []
        for line in result.stdout.splitlines():
            m = re.match(
                r"(?P<lineno>\d+):(?P<charno>\d+):\s+(?P<message>.*)", line
            )
            if m:
                messages.append(
                    LinterMessage(
                        tool=cls.name,
                        message_id="C901",
                        filename=str(file),
                        lineno=int(m.group("lineno")),
                        charno=int(m.group("charno")),
                        message=f"too complex: {m.group('message')}",
                        extramessage="",
                    )
                )
            else:
                print("ERROR parsing", line)

        return messages
