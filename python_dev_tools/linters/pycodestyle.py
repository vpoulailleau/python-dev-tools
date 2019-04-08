"""Pycodestyle linter management."""
from .common import Linter


class PycodestyleLinter(Linter):
    """Pycodestyle linter management."""

    name = "pycodestyle"
    path = "pycodestyle"
    regex = [
        r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
        r"\s+(?P<message_id>.*?)\s+(?P<message>.*)"
    ]
