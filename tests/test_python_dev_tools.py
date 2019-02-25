"""Tests for `python_dev_tools` package."""

from python_dev_tools.whatalinter import LinterMessage, lint, main


def test_main(tmpdir):
    import sys

    p = tmpdir.join("foo.py")
    p.write("a = 1\n")
    sys.argv = ["whatalinter", str(p)]
    main()


def test_long_line(tmpdir):
    p = tmpdir.join("foo.py")
    p.write('"' + 78 * "#" + '"\n')
    result = lint(p)
    assert result == {
        LinterMessage(
            tool="pycodestyle",
            message_id="E501",
            filename=str(p),
            lineno=1,
            charno=80,
            message="line too long (80 > 79 characters)",
            extramessage="",
        )
    }


def test_duplicate_key(tmpdir):
    p = tmpdir.join("foo.py")
    p.write("a = {1: 5, 1: 6}\n")
    result = lint(p)
    assert result == {
        LinterMessage(
            tool="PyFlakes",
            message_id="W999",
            filename=str(p),
            lineno=1,
            charno=0,
            message="dictionary key 1 repeated with different values",
            extramessage="",
        )
    }
