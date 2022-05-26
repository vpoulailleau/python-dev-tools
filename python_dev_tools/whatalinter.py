import ast
from typing import TYPE_CHECKING, Final, Type, List

import pkg_resources

if TYPE_CHECKING:
    from flake8.options.manager import OptionManager


MAX_LINE_LENGTH: Final = 88
MAX_COMPLEXITY: Final = 10
ERROR_CODE: Final = "WAL"


class WhatALinter:
    name = "whatalinter"
    version = pkg_resources.get_distribution("python_dev_tools").version

    def __init__(self: "WhatALinter", tree: ast.AST) -> None:
        """Empty method, needed by flake8.

        Args:
            tree (AST): unused
        """

    def run(self: "WhatALinter") -> List:
        """Empty method, needed by flake8.

        Returns:
            Empty list
        """
        return []

    @classmethod
    def add_options(cls: Type["WhatALinter"], parser: "OptionManager") -> None:
        """Add options to CLI parser.

        Args:
            parser (OptionManager): CLI parser
        """
        parser.extend_default_select([ERROR_CODE])
        parser.extend_default_ignore(
            [
                "E203",  # space around : in slice
                "WPS305",  # avoid f-strings
                "WPS306",  # required explicit subclassing of object
                "WPS421",  # Found wrong function call, useful in scripts
            ],
        )
        parser.parser.set_defaults(
            max_line_length=MAX_LINE_LENGTH,
            max_complexity=MAX_COMPLEXITY,
            inline_quotes='"',
        )
