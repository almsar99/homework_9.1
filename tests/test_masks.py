import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    result = get_mask_card_number("1234567890123456")
    assert result == "1234 56** **** 3456"


def test_get_mask_account():
    result = get_mask_account("1234567890123456")
    assert result == "**3456"


def test_get_mask_card_number_error():
    with pytest.raises(Exception):
        get_mask_card_number(None)  # type: ignore


def test_get_mask_account_error():
    with pytest.raises(Exception):
        get_mask_account(None)  # type: ignore
