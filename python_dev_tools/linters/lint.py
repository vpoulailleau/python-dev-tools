"""Definition of lint function, calling all linters."""

from .flake8 import Flake8Linter
from .mccabe import MccabeLinter
from .pycodestyle import PycodestyleLinter
from .pydocstyle import PydocstyleLinter
from .pyflakes import PyflakesLinter

linters = [
    PyflakesLinter,
    PycodestyleLinter,
    MccabeLinter,
    PydocstyleLinter,
    Flake8Linter,
]


def lint(filepath, all_warnings=False):
    """Lint the file with known linters."""
    messages = set()
    for linter in linters:
        messages.update(linter.lint(filepath))
        if len(messages) >= 10 and not all_warnings:
            break

    messages = sorted(list(messages))
    if all_warnings:
        return messages
    return messages[:10]
