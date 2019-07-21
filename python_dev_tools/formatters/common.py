"""Common constants and class to all linters."""
import subprocess


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
    def format_file(cls, filepath):
        """Execute the formatter."""
        try:
            return cls._format_file(filepath)
        except FormatterNotFound:
            print(f"Formatter {cls.name} not found: {cls.path}")

    @classmethod
    def _format_file(cls, filepath):
        args = [cls.path, *cls.cli_args, str(filepath)]
        cls._execute_command(args)

    @classmethod
    def _execute_command(cls, args):
        """Execute the formatter or raise FormatterNotFound."""
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
                raise FormatterNotFound
            else:
                raise
