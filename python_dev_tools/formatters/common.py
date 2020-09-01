"""Common constants and class to all linters."""
import subprocess  # noqa: S404
from typing import List


class FormatterNotFound(FileNotFoundError):
    """
    Exception to detect that a formatter is not found.

    Note that this doesn't occur, except due to an installation error.
    """


class Formatter:
    """Base formatter class."""

    name = "Formatter"
    path = "/bin/unknownformatter"
    cli_args = []

    @classmethod
    def format_file(cls, filepath: str) -> None:
        """Execute the formatter.

        Args:
            filepath (str): path of the file to format
        """
        try:
            cls._format_file(filepath)
        except FormatterNotFound:
            print(f"Formatter {cls.name} not found: {cls.path}")

    @classmethod
    def _format_file(cls, filepath: str):
        args = [cls.path, *cls.cli_args, filepath]
        cls._execute_command(args)

    @classmethod
    def _execute_command(cls, args: List[str]) -> subprocess.CompletedProcess:
        """Execute the formatter.

        Args:
            args (list[str]): arguments of the command including command name

        Raises:
            FormatterNotFound: formatter ``cls.path`` not found in path

        Returns:
            CompletedProcess: result of the execution
        """
        try:
            return subprocess.run(  # noqa: S603
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10,
                encoding="utf-8",
            )
        except FileNotFoundError as exc:
            if exc.filename == cls.path:
                raise FormatterNotFound
            raise
