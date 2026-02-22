import json
from unittest.mock import patch

from src.utils import load_transactions


def test_load_transactions_ok(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text(
        '[{"id": 1}, {"id": 2}]',
        encoding="utf-8",
    )

    result = load_transactions(str(file_path))

    assert isinstance(result, list)
    assert len(result) == 2


def test_load_transactions_not_exists():
    result = load_transactions("no_such_file.json")
    assert result == []


def test_load_transactions_not_list(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text(
        '{"id": 1}',
        encoding="utf-8",
    )

    result = load_transactions(str(file_path))
    assert result == []


@patch("src.utils.json.load")
def test_load_transactions_json_decode_error(mock_json):
    mock_json.side_effect = json.JSONDecodeError("error", "doc", 0)

    result = load_transactions("data/operations.json")

    assert result == []
