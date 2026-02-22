import os
from typing import Dict

import requests  # type: ignore[import-untyped]

API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rubles(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: словарь с данными транзакции
    :return: сумма в рублях
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_API_KEY")
    headers = {"apikey": api_key}

    response = requests.get(
        API_URL,
        headers=headers,
        params={"base": currency, "symbols": "RUB"},
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()
    rate = float(data["rates"]["RUB"])
    return amount * rate
