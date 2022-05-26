"""Linter module, flake8 plugin."""
import ast
from typing import TYPE_CHECKING, List, Type

import pkg_resources

if TYPE_CHECKING:
    import sys

    from flake8.options.manager import OptionManager

    if sys.version_info < (3, 8):
        from typing import Any as Final  # noqa: WPS433, WPS440
    else:
        from typing import Final  # noqa: WPS433, WPS440

else:
    from typing import Any as Final  # noqa: WPS440


MAX_LINE_LENGTH: Final = 88
MAX_COMPLEXITY: Final = 10
ERROR_CODE: Final = "WAL"


class WhatALinter:
    """WhatALinter flake8 plugin."""

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
            min_python_version="3.7.0",
            max_line_length=MAX_LINE_LENGTH,
            max_complexity=MAX_COMPLEXITY,
            inline_quotes='"',
        )
