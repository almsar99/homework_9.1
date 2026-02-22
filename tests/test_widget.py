from src.widget import get_date, mask_account_card


def test_mask_account_card_card():
    result = mask_account_card("Visa Platinum 1234567890123456")
    assert "****" in result


def test_mask_account_card_account():
    result = mask_account_card("Счет 1234567890123456")
    assert result.endswith("3456")


def test_get_date():
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"
