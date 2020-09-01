"""Definition of format function, calling all formatters."""
from typing import List

from python_dev_tools.formatters.autoflake import AutoflakeFormatter
from python_dev_tools.formatters.black import BlackFormatter
from python_dev_tools.formatters.common import Formatter
from python_dev_tools.formatters.pyupgrade import PyupgradeFormatter

formatters: List[Formatter] = [
    AutoflakeFormatter,
    PyupgradeFormatter,
    BlackFormatter,  # BlackFormatter should be the last one
]


def format_file(filepath: str) -> None:
    """Format the file with known formatters.

    Args:
        filepath (str): path of the file to format
    """
    for formatter in formatters:
        formatter.format_file(filepath)
