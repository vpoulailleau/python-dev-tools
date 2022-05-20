import pkg_resources


class WhatALinter:
    name = "whatalinter"
    version = pkg_resources.get_distribution("python_dev_tools").version

    def __init__(self, tree):
        pass

    def run(self):
        return []

    @classmethod
    def add_options(cls, parser):
        ERROR_CODE = "WAL"
        parser.extend_default_select([ERROR_CODE])
        # TODO --max-line-length 88
        # TODO --max-complexity 10
        parser.extend_default_ignore(
            [
                "E203",  # space around : in slice
                # TODO configure flake8-quotes --inline-quotes '"'
                "Q000",  # Remove bad quotes
                "WPS305",  # avoid f-strings
                "WPS306",  # required explicit subclassing of object
                # "WPS602",  # avoid @staticmethod (can be subclassed…)
            ]
        )
