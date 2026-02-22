from unittest.mock import patch

import pandas as pd

from src.readers import load_transactions_from_csv, load_transactions_from_excel


@patch("src.readers.pd.read_csv")
def test_load_transactions_from_csv(mock_read_csv):
    mock_df = pd.DataFrame(
        [
            {"id": 1, "amount": 100},
            {"id": 2, "amount": 200},
        ]
    )

    mock_read_csv.return_value = mock_df

    result = load_transactions_from_csv("fake.csv")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1


@patch("src.readers.pd.read_excel")
def test_load_transactions_from_excel(mock_read_excel):
    mock_df = pd.DataFrame(
        [
            {"id": 10, "amount": 500},
            {"id": 20, "amount": 600},
        ]
    )

    mock_read_excel.return_value = mock_df

    result = load_transactions_from_excel("fake.xlsx")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[1]["id"] == 20


@patch("src.readers.pd.read_csv")
def test_load_csv_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError

    result = load_transactions_from_csv("missing.csv")

    assert result == []


@patch("src.readers.pd.read_excel")
def test_load_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError

    result = load_transactions_from_excel("missing.xlsx")

    assert result == []


@patch("src.readers.pd.read_csv")
def test_load_csv_unexpected_exception(mock_read_csv):
    mock_read_csv.side_effect = Exception("Unexpected error")

    result = load_transactions_from_csv("broken.csv")

    assert result == []


@patch("src.readers.pd.read_excel")
def test_load_excel_unexpected_exception(mock_read_excel):
    mock_read_excel.side_effect = Exception("Unexpected error")

    result = load_transactions_from_excel("broken.xlsx")

    assert result == []
