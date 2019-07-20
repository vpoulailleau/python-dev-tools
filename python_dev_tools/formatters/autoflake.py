"""Autoflake formatter management."""
from .common import Formatter


class AutoflakeFormatter(Formatter):
    """Autoflake formatter management."""

    name = "autoflake"
    path = "autoflake"
    cli_args = ["--in-place", "--remove-unused-variables"]
