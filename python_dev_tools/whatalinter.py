"""Linter module"""
import argparse
import re
import subprocess
from collections import namedtuple

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
    def __str__(self):
        return (
            f"{self.filename}:{self.lineno}:{self.charno}: "
            f"[{self.tool}] {self.message} {self.extramessage}"
        )


class Linter:
    name = "Linter"
    path = "/bin/unknownlinter"

    @classmethod
    def lint(cls, file):
        """Execute the linter and return the list of messages"""
        return []

    @classmethod
    def _execute_command(cls, args):
        return subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10,
            encoding="utf-8",
        )


class PycodestyleLinter(Linter):
    name = "pycodestyle"
    path = "pycodestyle"

    @classmethod
    def lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        for line in result.stdout.splitlines():
            m = re.match(r"(.*?):(\d+):(\d+):\s+(.*?)\s+(.*)", line)
            if m:
                messages.append(
                    LinterMessage(
                        tool="pycodestyle",
                        message_id=m.group(4),
                        filename=m.group(1),
                        lineno=int(m.group(2)),
                        charno=int(m.group(3)),
                        message=m.group(5),
                        extramessage="",
                    )
                )
            else:
                print("ERROR parsing", line)

        return messages


def main():
    parser = argparse.ArgumentParser(
        description="Python linter combining existing linters"
    )
    parser.add_argument(
        "file", metavar="FILE", type=str, help="path of the file to lint"
    )
    parser.add_argument(
        "-f",
        "--first",
        action="store_true",
        default=False,
        help="[TODO] stop early if 10+ warnings are found",
    )
    args = parser.parse_args()

    linters = [PycodestyleLinter]
    messages = set()
    for linter in linters:
        messages.update(linter.lint(args.file))
    for message in messages:
        print(message)


if __name__ == "__main__":
    main()
