import json
from typing import Any


def load_transactions(path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param path: путь к JSON-файлу
    :return: список словарей с транзакциями
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return []
