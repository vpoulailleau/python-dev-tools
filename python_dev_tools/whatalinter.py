"""Linter module"""
import argparse
import subprocess
from collections import namedtuple

LinterMessage = namedtuple(
    "LinterMessage",
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
    path = "/home/vincent/documents/programmation/python-dev-tools/venv/bin/pycodestyle"

    @classmethod
    def lint(cls, file):
        args = [cls.path, str(file)]
        result = cls._execute_command(args)
        messages = []
        for line in result.stdout.splitlines():
            messages.append(
                LinterMessage(
                    tool="pycodestyle",
                    message_id="123",
                    filename="123",
                    lineno=123,
                    charno=123,
                    message=line,
                    extramessage="",
                )
            )

        return messages


def lint(file, linters):
    result = set()
    for linter in linters:
        result.update(linter.lint(file))
    return result


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
        help="stop early if 10+ warnings are found",
    )

    args = parser.parse_args()

    linters = [PycodestyleLinter()]

    print(lint(args.file, linters))


if __name__ == "__main__":
    main()
