"""Common constants and class to all linters."""
import subprocess  # noqa: S404
from typing import List, NamedTuple


class FormatterConfig(NamedTuple):
    """Configuration of formatting tool."""

    name: str
    path: str
    cli_args: List[str]


_formatters_configs: List[FormatterConfig] = [
    FormatterConfig(
        name="autoflake",
        path="autoflake",
        cli_args=["--in-place", "--remove-unused-variables"],
    ),
    FormatterConfig(name="pyupgrade", path="pyupgrade", cli_args=["--py37-plus"]),
    FormatterConfig(
        name="black",
        path="black",
        cli_args=["--target-version=py37"],
    ),  # Should be the last config
]


def _format_file(filepath: str, config: FormatterConfig) -> None:
    """Execute the formatter.

    Args:
        filepath (str): path of the file to format
        config (FormatterConfig): configuration for the formatting tool

    Returns:
        None
    """
    try:
        return subprocess.run(  # noqa: S603
            [config.path, *config.cli_args, filepath],
            capture_output=True,
            timeout=10,
            encoding="utf-8",
        )
    except FileNotFoundError as exc:
        if exc.filename == config.path:
            print(f"Formatter {config.name} not found: {config.path}")


def format_file(filepath: str) -> None:
    """Format the file with known formatters.

    Args:
        filepath (str): path of the file to format
    """
    for config in _formatters_configs:
        _format_file(filepath, config)
