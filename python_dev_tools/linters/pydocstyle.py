"""Pydocstyle linter management."""
from .common import Linter


class PydocstyleLinter(Linter):
    """Pydocstyle linter management."""

    name = "pydocstyle"
    path = "pydocstyle"
    regex = [
        r"(?P<filename>.*?):(?P<lineno>\d+)\s+(?P<extramessage>.*):",
        r"\s*(?P<message_id>D\d+):\s+(?P<message>.*)",
    ]
