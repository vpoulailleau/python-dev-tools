"""Black formatter management."""
from python_dev_tools.formatters.common import Formatter


class BlackFormatter(Formatter):
    """Black formatter management."""

    name = "black"
    path = "black"
    cli_args = ["--target-version=py36"]
