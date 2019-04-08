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
    p.write('"""Docstring."""\n\naaa = {1: 5, 1: 6}\n')
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
            charno=8,
            message="dictionary key 1 repeated with different values",
            extramessage="",
        ),
        LinterMessage(
            tool="flake8",
            message_id="F601",
            filename=str(p),
            lineno=3,
            charno=14,
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
    result = lint(p)
    assert result == [
        LinterMessage(
            tool="McCabe",
            message_id="C901",
            filename=str(p),
            lineno=7,
            charno=0,
            message="too complex: 'foo' 11",
            extramessage="",
        )
    ]


def test_no_docstring(tmpdir):
    """Test pydocstyle is working."""
    p = tmpdir.join("foo.py")
    p.write("aaa = 3\n")
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
        content += f"{char}{char}{char} = {char}{char}{char}\n"
    p.write(content)
    result = lint(p, all_warnings=True)
    assert len(result) == 2 * len(chars) + 1


def test_not_all_warnings(tmpdir):
    """Test all_warnings disabled in lint."""
    p = tmpdir.join("foo.py")
    chars = "ABCDEFGJKLMNP"
    content = ""
    for char in chars:
        content += f"{char}{char}{char} = {char}{char}{char}\n"
    p.write(content)
    result = lint(p, all_warnings=False)
    assert len(result) == 10


def test_lint_myself():
    """Test no lint message for this project."""
    source_dir = Path("python_dev_tools")
    print()
    results = []
    for python_file in source_dir.rglob("*.py"):
        result = lint(python_file, all_warnings=True)
        print(python_file, result)
        results.extend(result)
    assert results == [
        LinterMessage(
            tool="flake8",
            message_id="S404",
            filename="python_dev_tools/linters/common.py",
            lineno=4,
            charno=1,
            message="Consider possible security implications associated with subprocess module.",
            extramessage="",
        ),
        LinterMessage(
            tool="flake8",
            message_id="T101",
            filename="python_dev_tools/linters/common.py",
            lineno=10,
            charno=3,
            message="fixme found (TODO)",
            extramessage="",
        ),
        LinterMessage(
            tool="flake8",
            message_id="S603",
            filename="python_dev_tools/linters/common.py",
            lineno=122,
            charno=1,
            message="subprocess call - check for execution of untrusted input.",
            extramessage="",
        ),
    ]


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
