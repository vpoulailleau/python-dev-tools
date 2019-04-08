"""Tests for `python_dev_tools` package."""
from pathlib import Path
from textwrap import dedent

import python_dev_tools.whatalinter
from python_dev_tools.linters.common import LinterMessage
from python_dev_tools.linters.lint import lint, linters
from python_dev_tools.whatalinter import main


def test_main(tmpdir, capsys):
    """Test main call."""
    import sys

    p = tmpdir.join("foo.py")
    p.write("a = 1\n")
    sys.argv = ["whatalinter", str(p)]
    python_dev_tools.whatalinter.__name__ = "__main__"
    main()
    captured = capsys.readouterr()
    assert "[pydocstyle] Missing docstring in public module" in captured.out


def test_str_message():
    """Test message formatting."""
    msg = LinterMessage(
        tool="foo",
        message_id="bar",
        filename="baz",
        lineno=1,
        charno=2,
        message="msg)",
        extramessage="extra msg",
    )
    assert str(msg) == "baz:1:2: War [foo] msg) (extra msg)"


def test_long_line(tmpdir):
    """Test pycodestyle is working."""
    p = tmpdir.join("foo.py")
    p.write('"""Docstring."""\n\n"' + 78 * "#" + '"\n')
    result = lint(p)
    assert result == [
        LinterMessage(
            tool="pycodestyle",
            message_id="E501",
            filename=str(p),
            lineno=3,
            charno=80,
            message="line too long (80 > 79 characters)",
            extramessage="",
        )
    ]


def test_duplicate_key(tmpdir):
    """Test pyflakes is working."""
    p = tmpdir.join("foo.py")
    p.write('"""Docstring."""\n\na = {1: 5, 1: 6}\n')
    result = lint(p)
    assert result == [
        LinterMessage(
            tool="pyflakes",
            message_id="W999",
            filename=str(p),
            lineno=3,
            charno=1,
            message="dictionary key 1 repeated with different values",
            extramessage="",
        ),
        LinterMessage(
            tool="flake8",
            message_id="F601",
            filename=str(p),
            lineno=3,
            charno=6,
            message="dictionary key 1 repeated with different values",
            extramessage="",
        ),
        LinterMessage(
            tool="flake8",
            message_id="F601",
            filename=str(p),
            lineno=3,
            charno=12,
            message="dictionary key 1 repeated with different values",
            extramessage="",
        ),
    ]


def test_complexity(tmpdir):
    """Test McCabe is working."""
    p = tmpdir.join("foo.py")
    file_content = '"""Docstring."""\n\n'
    file_content += dedent(
        """
        from random import randint

        elements = [randint(0, 1) for _ in range(10)]


        def foo():
            \"\"\"Docstring.\"\"\"
            if elements[0]:
                a = 1
            elif elements[1]:
                a = 1
            elif elements[2]:
                a = 1
            elif elements[3]:
                a = 1
            elif elements[4]:
                a = 1
            elif elements[5]:
                a = 1
            elif elements[6]:
                a = 1
            elif elements[7]:
                a = 1
            elif elements[8]:
                a = 1
            elif elements[9]:
                a = 1
            print(a)
    """
    )
    p.write(file_content)
    result = lint(p)
    assert result == [
        LinterMessage(
            tool="McCabe",
            message_id="C901",
            filename=str(p),
            lineno=9,
            charno=0,
            message="too complex: 'foo' 11",
            extramessage="",
        )
    ]


def test_no_docstring(tmpdir):
    """Test pydocstyle is working."""
    p = tmpdir.join("foo.py")
    p.write("a = 3\n")
    result = lint(p)
    assert result == [
        LinterMessage(
            tool="pydocstyle",
            message_id="D100",
            filename=str(p),
            lineno=1,
            charno=1,
            message="Missing docstring in public module",
            extramessage="at module level",
        )
    ]


def test_all_warnings(tmpdir):
    """Test all_warnings enabled in lint."""
    p = tmpdir.join("foo.py")
    chars = "ABCDEFGJKLMNP"
    content = ""
    for char in chars:
        content += f"{char} = {char}\n"
    p.write(content)
    result = lint(p, all_warnings=True)
    assert len(result) == 2 * len(chars) + 1


def test_not_all_warnings(tmpdir):
    """Test all_warnings disabled in lint."""
    p = tmpdir.join("foo.py")
    chars = "ABCDEFGJKLMNP"
    content = ""
    for char in chars:
        content += f"{char} = {char}\n"
    p.write(content)
    result = lint(p, all_warnings=False)
    assert len(result) == 10


def test_lint_myself():
    """Test no lint message for this project."""
    source_dir = Path("python_dev_tools")
    print()
    for python_file in source_dir.rglob("*.py"):
        result = lint(python_file, all_warnings=True)
        print(python_file, result)
        assert not result


def test_installation_error(tmpdir):
    """
    Test for installation error, with missing executable.

    Useless test, except for coverage or installation error.
    """
    for linter_class in linters:
        linter_class.path = "unknown"
    p = tmpdir.join("foo.py")
    p.write("a = 3\n")
    lint(p)
