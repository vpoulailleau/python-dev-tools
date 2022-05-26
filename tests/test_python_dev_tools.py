"""Tests for `python_dev_tools` package."""
import sys
from pathlib import Path
from textwrap import dedent

import pytest
from flake8.api import legacy as flake8

import python_dev_tools
from python_dev_tools.whataformatter import main as main_formatter


def test_main_formatter(tmpdir):
    """Test main call."""
    p = tmpdir.join("foo.py")
    p.write(
        dedent(
            """
            a =   1
            """
        )
    )
    sys.argv = ["whataformatter", str(p)]
    python_dev_tools.whataformatter.__name__ = "__main__"

    main_formatter()

    # TODO assert file content


# TODO test formatting


def run_linter(
    tmp_path: Path, capsys, file_content: str, expected_message: str
) -> None:
    tmp_file = tmp_path / ("foo.py")
    tmp_file.write_text(file_content, encoding="utf-8")

    linter = flake8.get_style_guide()
    linter.check_files([str(tmp_file)])

    assert expected_message in capsys.readouterr().out


def test_main_linter(tmp_path: Path, capsys):
    """Test main call."""
    run_linter(tmp_path, capsys, "a = 1\n", "Missing docstring in public module")


def test_long_line(tmp_path: Path, capsys):
    """Test pycodestyle is working."""
    run_linter(
        tmp_path,
        capsys,
        '"""Docstring."""\n\n"' + 87 * "#" + '"\n',
        "line too long (89 > 88 characters)",
    )


def test_duplicate_key(tmp_path: Path, capsys):
    """Test pyflakes is working."""
    run_linter(
        tmp_path,
        capsys,
        '"""Docstring."""\n\naaa = {1: 5, 1: 6}\n',
        "dictionary key 1 repeated with different values",
    )


def test_complexity(tmp_path: Path, capsys):
    """Test McCabe is working."""
    file_content = '"""Docstring."""\n\n'
    file_content += dedent(
        """
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
    )
    run_linter(tmp_path, capsys, file_content, "'foo' is too complex (11)")


def test_lint_myself(capsys):
    """Test no lint message for this project."""
    source_dir = Path("python_dev_tools")
    if not source_dir.exists():
        # run from inside tests directory
        source_dir = Path("../python_dev_tools")

    linter = flake8.get_style_guide()
    linter.check_files([str(path) for path in source_dir.rglob("*.py")])

    captured = capsys.readouterr()
    assert captured.out.replace("../", "") == dedent(
        """\
        python_dev_tools/whataformatter.py:122:7: T101 fixme found (TODO)
        """
    )
