"""Definition of format function, calling all formatters."""

from .black import BlackFormatter

formatters = [BlackFormatter]


def format_file(filepath):
    """Format the file with known formatters."""
    for formatter in formatters:
        formatter.format_file(filepath)
