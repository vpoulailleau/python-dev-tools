import pkg_resources
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flake8.options.manager import OptionManager


class WhatALinter:
    name = "whatalinter"
    version = pkg_resources.get_distribution("python_dev_tools").version

    def __init__(self, tree):
        pass

    def run(self):
        return []

    @classmethod
    def add_options(cls, parser: "OptionManager"):
        ERROR_CODE = "WAL"
        parser.extend_default_select([ERROR_CODE])
        parser.extend_default_ignore(
            [
                "E203",  # space around : in slice
                "WPS305",  # avoid f-strings
                "WPS306",  # required explicit subclassing of object
                "WPS421",  # Found wrong function call, useful in scripts
                # "WPS602",  # avoid @staticmethod (can be subclassed…)
            ]
        )
        parser.parser.set_defaults(
            max_line_length=88, max_complexity=10, inline_quotes='"'
        )
