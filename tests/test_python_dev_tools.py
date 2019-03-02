"""Tests for `python_dev_tools` package."""
from pathlib import Path

from python_dev_tools.whatalinter import LinterMessage, lint, main


def test_main(tmpdir):
    import sys

    p = tmpdir.join("foo.py")
    p.write("a = 1\n")
    sys.argv = ["whatalinter", str(p)]
    main()


def test_str_message():
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
        )
    ]


# TODO test mccabe


def test_no_docstring(tmpdir):
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


def test_lint_myself():
    source_dir = Path("python_dev_tools")
    for python_file in source_dir.rglob("*.py"):
        assert not lint(python_file)
