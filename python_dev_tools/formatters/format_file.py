"""Definition of format function, calling all formatters."""

from .autoflake import AutoflakeFormatter
from .black import BlackFormatter

formatters = [
    AutoflakeFormatter,
    BlackFormatter,
]  # BlackFormatter should be the last one


def format_file(filepath):
    """Format the file with known formatters."""
    for formatter in formatters:
        formatter.format_file(filepath)
