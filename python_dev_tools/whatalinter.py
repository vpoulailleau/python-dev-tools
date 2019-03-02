"""Linter module, aggregation of linters."""
import argparse
import os
import pathlib
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
    """Generic linter message."""

    def __str__(self):
        """Represent as a string."""
        return self.formatted(_DEFAULT_MESSAGE_FORMAT)

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


def lint(file, all_warnings=False):
    """Lint the file with known linters."""
    linters = [
        PyflakesLinter,
        PycodestyleLinter,
        MccabeLinter,
        PydocstyleLinter,
    ]
    messages = set()
    for linter in linters:
        messages.update(linter.lint(file))
        if len(messages) >= 10:
            break

    messages = sorted(list(messages))
    return messages[:10]


def udpate_os_path():
    """Update PATH env variable to find linters."""
    script_path = pathlib.Path(__file__).resolve()
    os.environ["PATH"] = "".join(
        (str(script_path.parent), os.pathsep, os.environ["PATH"])
    )

    # replace /lib/ with /bin/, and add to PATH
    for parent in reversed(script_path.parents):
        if parent.stem == "lib":
            os.environ["PATH"] = "".join(
                (str(parent.parent / "bin"), os.pathsep, os.environ["PATH"])
            )


def main():
    """Entry point."""
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
        "-a",
        "--all",
        action="store_true",
        default=False,
        help="Display all warnings (default: display first ten warnings)",
    )
    args = parser.parse_args()

    udpate_os_path()
    for message in lint(file=args.file, all_warnings=args.all):
        print(message.formatted(args.format))


if __name__ == "__main__":
    main()
