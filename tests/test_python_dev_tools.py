"""Tests for `python_dev_tools` package."""
import sys
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING

from flake8.api import legacy as flake8

import python_dev_tools
from python_dev_tools.whataformatter import main as main_formatter

if TYPE_CHECKING:
    from typing import Final  # noqa: WPS433, WPS440
else:
    from typing import Any as Final  # noqa: WPS440


def test_main_formatter(tmp_path: Path) -> None:
    """Test main call.

    Args:
        tmp_path (Path): temporary directory where to create file
    """
    checked_file = tmp_path / ("foo.py")
    checked_file.write_text("a =   1", encoding="utf-8")
    sys.argv = ["whataformatter", str(checked_file)]
    python_dev_tools.whataformatter.__name__ = "__main__"

    main_formatter()

    assert checked_file.read_text(encoding="utf-8") == "a = 1\n"


def test_main_formatter_diff(tmp_path: Path, capsys) -> None:
    """Test main call.

    Args:
        tmp_path (Path): temporary directory where to create files
    """
    checked_file = tmp_path / ("foo.py")
    checked_file.write_text("a =   1", encoding="utf-8")
    sys.argv = ["whataformatter", "--diff", str(checked_file)]
    python_dev_tools.whataformatter.__name__ = "__main__"

    main_formatter()

    captured = capsys.readouterr()
    assert captured.err == ""
    assert "-a =   1\n+a = 1\n" in captured.out


def run_linter(
    tmp_path: Path,
    capsys,
    file_content: str,
    expected_message: str,
) -> None:
    """Help to run linter on temporary file.

    Args:
        tmp_path (Path): temporary directory where to create files
        capsys: pytest fixture
        file_content (str): content to be written in a temporary file
        expected_message (str): expected linter report
    """
    tmp_file = tmp_path / ("foo.py")
    tmp_file.write_text(file_content, encoding="utf-8")

    linter = flake8.get_style_guide()
    linter.check_files([str(tmp_file)])

    assert expected_message in capsys.readouterr().out


def test_main_linter(tmp_path: Path, capsys) -> None:
    """Test main call.

    Args:
        tmp_path (Path): temporary directory where to create files
        capsys: pytest fixture
    """
    run_linter(tmp_path, capsys, "a = 1\n", "Missing docstring in public module")


def test_long_line(tmp_path: Path, capsys) -> None:
    """Test pycodestyle is working.

    Args:
        tmp_path (Path): temporary directory where to create files
        capsys: pytest fixture
    """
    line_length: Final = 89
    docstring = '"""Docstring."""\n\n'
    long_line = line_length * "#"
    run_linter(
        tmp_path,
        capsys,
        f"{docstring}{long_line}\n",
        f"line too long ({line_length} > 88 characters)",
    )


def test_duplicate_key(tmp_path: Path, capsys) -> None:
    """Test pyflakes is working.

    Args:
        tmp_path (Path): temporary directory where to create files
        capsys: pytest fixture
    """
    run_linter(
        tmp_path,
        capsys,
        '"""Docstring."""\n\naaa = {1: 5, 1: 6}\n',
        "dictionary key 1 repeated with different values",
    )


def test_complexity(tmp_path: Path, capsys) -> None:
    """Test McCabe is working.

    Args:
        tmp_path (Path): temporary directory where to create files
        capsys: pytest fixture
    """
    file_content = '"""Docstring."""\n\n'
    program = """
        elements = [open(str(i)) for i in range(10)]


        def foo():
            \"\"\"Docstring.\"\"\"
            if elements[0]:
                aaa = 1
            elif elements[1]:
                aaa = 1
            elif elements[2]:
                aaa = 1
            elif elements[3]:
                aaa = 1
            elif elements[4]:
                aaa = 1
            elif elements[5]:
                aaa = 1
            elif elements[6]:
                aaa = 1
            elif elements[7]:
                aaa = 1
            elif elements[8]:
                aaa = 1
            elif elements[9]:
                aaa = 1
            print(aaa)
    """
    file_content += dedent(program)
    run_linter(tmp_path, capsys, file_content, "'foo' is too complex (11)")


def test_lint_myself(capsys) -> None:
    """Test no lint message for this project.

    Args:
        capsys: pytest fixture
    """
    source_dir = Path("python_dev_tools")
    if not source_dir.exists():
        # run from inside tests directory
        source_dir = Path("../python_dev_tools")
    linter = flake8.get_style_guide()

    linter.check_files([str(path) for path in source_dir.rglob("*.py")])

    captured = capsys.readouterr().out.replace("../", "").replace("\\", "/")
    assert captured == ""
