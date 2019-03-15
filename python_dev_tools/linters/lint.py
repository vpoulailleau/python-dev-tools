"""Definition of lint function, calling all linters."""

from python_dev_tools.linters.mccabe import MccabeLinter
from python_dev_tools.linters.pycodestyle import PycodestyleLinter
from python_dev_tools.linters.pydocstyle import PydocstyleLinter
from python_dev_tools.linters.pyflakes import PyflakesLinter

linters = [PyflakesLinter, PycodestyleLinter, MccabeLinter, PydocstyleLinter]


def lint(file, all_warnings=False):
    """Lint the file with known linters."""
    messages = set()
    for linter in linters:
        messages.update(linter.lint(file))
        if len(messages) >= 10:
            break

    messages = sorted(list(messages))
    return messages[:10]
