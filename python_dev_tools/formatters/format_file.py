"""Definition of format function, calling all formatters."""

from python_dev_tools.formatters.autoflake import AutoflakeFormatter
from python_dev_tools.formatters.black import BlackFormatter
from python_dev_tools.formatters.pyupgrade import PyupgradeFormatter

formatters = [
    AutoflakeFormatter,
    PyupgradeFormatter,
    BlackFormatter,  # BlackFormatter should be the last one
]


def format_file(filepath):
    """Format the file with known formatters."""
    for formatter in formatters:
        formatter.format_file(filepath)
