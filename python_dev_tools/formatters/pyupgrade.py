"""Pyupgrade formatter management."""
from .common import Formatter


class PyupgradeFormatter(Formatter):
    """Pyupgrade formatter management."""

    name = "pyupgrade"
    path = "pyupgrade"
    cli_args = ["--py36-plus"]
