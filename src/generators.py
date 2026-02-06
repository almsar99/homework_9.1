"""
Модуль generators содержит генераторы для обработки транзакций.
"""

from typing import Iterator, Dict, Any, List


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency_code: str
) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по коду валюты.

    :param transactions: список транзакций
    :param currency_code: код валюты (например, 'USD')
    :return: итератор транзакций с указанной валютой
    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code") == currency_code
        ):
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    :param transactions: список транзакций
    :return: итератор описаний транзакций
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение
    :param stop: конечное значение
    :return: итератор номеров карт
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield " ".join(
            [
                card_number[0:4],
                card_number[4:8],
                card_number[8:12],
                card_number[12:16],
            ]
        )
