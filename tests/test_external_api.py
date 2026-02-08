from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles


def test_convert_rub_without_api():
    transaction = {
        "operationAmount": {
            "amount": "500.0",
            "currency": {"code": "RUB"},
        }
    }

    result = convert_to_rubles(transaction)

    assert result == 500.0


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {"RUB": 100.0}
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "10.0",
            "currency": {"code": "USD"},
        }
    }

    result = convert_to_rubles(transaction)

    assert result == 1000.0


@patch("src.external_api.requests.get")
def test_convert_eur_to_rub(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {"RUB": 110.0}
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "2.0",
            "currency": {"code": "EUR"},
        }
    }

    result = convert_to_rubles(transaction)

    assert result == 220.0
