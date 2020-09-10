"""Tests for `python_dev_tools` package."""
import sys
from pathlib import Path
from textwrap import dedent

import python_dev_tools.whataformatter
import python_dev_tools.whatalinter
from python_dev_tools.whataformatter import main as main_formatter
from python_dev_tools.whatalinter import lint, main as main_linter


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


def test_main_linter(tmpdir, capsys):
    """Test main call."""
    p = tmpdir.join("foo.py")
    p.write("a = 1\n")
    sys.argv = ["whatalinter", str(p)]
    python_dev_tools.whatalinter.__name__ = "__main__"

    main_linter()

    captured = capsys.readouterr()
    assert "Missing docstring in public module" in captured.out


def test_long_line(tmpdir, capsys):
    """Test pycodestyle is working."""
    p = tmpdir.join("foo.py")
    p.write('"""Docstring."""\n\n"' + 87 * "#" + '"\n')

    lint(p)

    captured = capsys.readouterr()
    assert "line too long (89 > 88 characters)" in captured.out


def test_duplicate_key(tmpdir, capsys):
    """Test pyflakes is working."""
    p = tmpdir.join("foo.py")
    p.write('"""Docstring."""\n\naaa = {1: 5, 1: 6}\n')

    lint(p)

    captured = capsys.readouterr()
    assert "dictionary key 1 repeated with different values" in captured.out


def test_complexity(tmpdir, capsys):
    """Test McCabe is working."""
    p = tmpdir.join("foo.py")
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
    p.write(file_content)

    lint(p)

    captured = capsys.readouterr()
    assert "'foo' is too complex (11)" in captured.out


def test_lint_myself(capsys):
    """Test no lint message for this project."""
    source_dir = Path("python_dev_tools")

    lint(source_dir)

    captured = capsys.readouterr()
    assert captured.out == dedent(
        """\
        python_dev_tools/whataformatter.py:0:1: WPS226 Found string constant over-use: PATH > 3
        python_dev_tools/whataformatter.py:26:1: WPS213 Found too many expressions: 10 > 9
        python_dev_tools/whatalinter.py:0:1: WPS202 Found too many module members: 9 > 7
        python_dev_tools/whatalinter.py:13:28: WPS323 Found `%` string formatting
        python_dev_tools/whatalinter.py:72:13: WPS420 Found wrong keyword: pass
        python_dev_tools/whatalinter.py:72:21: T101 fixme found (TODO)
        python_dev_tools/whatalinter.py:93:7: T101 fixme found (TODO)
        """
    )
