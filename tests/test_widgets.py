from app.lib.widgets import IntLineEdit
from pytestqt.qtbot import QtBot
import pytest


@pytest.mark.parametrize(
    "text, expected",
    [("1.5", "1"), ("9", "5"), ("-90", "0"), ("50", "5"), ("2", "2"), ("abc", "")],
)
def test_int_line_edit(qtbot: QtBot, text: str, expected: str) -> None:
    line_edit = IntLineEdit(min_value=0, max_value=5)
    qtbot.keyClicks(line_edit, text)
    line_edit.clearFocus()
    assert line_edit.text() == expected
