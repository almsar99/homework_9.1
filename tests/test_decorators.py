import pytest

from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)

    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_error_to_file(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    content = log_file.read_text(encoding="utf-8")

    assert "div error" in content
    assert "Inputs: (1, 0)" in content
