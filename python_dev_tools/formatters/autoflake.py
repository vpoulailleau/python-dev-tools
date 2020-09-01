"""Autoflake formatter management."""
from python_dev_tools.formatters.common import Formatter


class AutoflakeFormatter(Formatter):
    """Autoflake formatter management."""

    name = "autoflake"
    path = "autoflake"
    cli_args = ["--in-place", "--remove-unused-variables"]
