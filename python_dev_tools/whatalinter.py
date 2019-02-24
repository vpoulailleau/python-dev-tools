"""Linter module"""
import argparse
import subprocess

# TODO class result


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
        return []


def lint(file, linters):
    for linter in linters:
        linter.lint(file)


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

    lint(args.file, linters)


if __name__ == "__main__":
    main()
