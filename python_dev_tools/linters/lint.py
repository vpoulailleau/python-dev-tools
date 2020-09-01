"""Definition of lint function, calling all linters."""

from python_dev_tools.linters.flake8 import Flake8Linter

linters = [
    Flake8Linter,
]


def lint(filepath, all_warnings=False):
    """Lint the file with known linters."""
    messages = set()
    for linter in linters:
        messages.update(linter.lint(filepath))
        if len(messages) >= 10 and not all_warnings:
            break

    messages = sorted(messages)
    if all_warnings:
        return messages
    return messages[:10]
