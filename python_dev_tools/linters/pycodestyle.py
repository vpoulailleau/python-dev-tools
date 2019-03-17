"""Pycodestyle linter management."""
from python_dev_tools.linters.common import Linter


class PycodestyleLinter(Linter):
    """Pycodestyle linter management."""

    name = "pycodestyle"
    path = "pycodestyle"
    regex = [
        r"(?P<filename>.*?):(?P<lineno>\d+):(?P<charno>\d+):"
        r"\s+(?P<message_id>.*?)\s+(?P<message>.*)"
    ]
