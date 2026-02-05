import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
        ("Счет 1234567890123456", "Счет **3456"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ],
)
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected
