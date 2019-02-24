"""Tests for `python_dev_tools` package."""

from python_dev_tools.whatalinter import LinterMessage, lint


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
