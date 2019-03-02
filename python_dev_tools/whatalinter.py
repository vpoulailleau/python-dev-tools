"""Linter module"""
import argparse
import re
import subprocess
from collections import namedtuple

_DEFAULT_MESSAGE_FORMAT = "%(path)s:%(row)d:%(col)d: %(code)s %(text)s"

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
        return self.formatted(_DEFAULT_MESSAGE_FORMAT)

    def formatted(self, format):
        data = {
            "path": self.filename,
            "row": self.lineno,
            "col": self.charno,
            "code": self.message_id,
            "text": f"[{self.tool}] {self.message}",
        }
        if self.extramessage:
            data["text"] += f" ({self.extramessage})"

        return format % data


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
            m = re.match(
                r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
                r"\s+(?P<message_id>.*?)\s+(?P<message>.*)",
                line,
            )
            if m:
                messages.append(
                    LinterMessage(
                        tool=cls.name,
                        message_id=m.group("message"),
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


class PyflakesLinter(Linter):
    name = "pyflakes"
    path = "pyflakes"

    @classmethod
    def lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        for line in result.stdout.splitlines():
            m = re.match(
                r"(?P<filename>.*?):(?P<lineo>\d+):\s+(?P<message>.*)", line
            )
            if m:
                messages.append(
                    LinterMessage(
                        tool=cls.name,
                        message_id="W999",
                        filename=m.group("filename"),
                        lineno=int(m.group("lineno")),
                        charno=0,
                        message=m.group("message"),
                        extramessage="",
                    )
                )
            else:
                print("ERROR parsing", line)

        return messages


class MccabeLinter(Linter):
    name = "McCabe"
    max_complexity = 10

    @classmethod
    def lint(cls, file):
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


def lint(file):
    linters = [PyflakesLinter, PycodestyleLinter, MccabeLinter]
    messages = set()
    for linter in linters:
        messages.update(linter.lint(file))
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
        "--format",
        default=_DEFAULT_MESSAGE_FORMAT,
        help="format of the output",
    )
    parser.add_argument(
        "-s",
        "--first",
        action="store_true",
        default=False,
        help="[TODO] stop early if 10+ warnings are found",
    )
    args = parser.parse_args()

    for message in lint(args.file):
        print(message.formatted(args.format))


if __name__ == "__main__":
    main()
