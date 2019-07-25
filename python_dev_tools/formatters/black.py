"""Black formatter management."""
from .common import Formatter


class BlackFormatter(Formatter):
    """Black formatter management."""

    name = "black"
    path = "black"
    cli_args = ["--line-length", "79", "--target-version=py36"]
