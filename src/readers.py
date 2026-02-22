import logging
from typing import Any

import pandas as pd


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def load_transactions_from_csv(path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    :param path: путь к CSV-файлу
    :return: список словарей с транзакциями
    """
    try:
        logger.debug("Reading CSV file: %s", path)

        df = pd.read_csv(path)

        transactions: list[dict[str, Any]] = df.to_dict(orient="records")

        logger.debug("Successfully loaded %d records from CSV", len(transactions))
        return transactions

    except FileNotFoundError:
        logger.error("CSV file not found: %s", path)
        return []

    except Exception as error:
        logger.error("Error reading CSV file %s: %s", path, error)
        return []


def load_transactions_from_excel(path: str) -> list[dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    :param path: путь к Excel-файлу
    :return: список словарей с транзакциями
    """
    try:
        logger.debug("Reading Excel file: %s", path)

        df = pd.read_excel(path)

        transactions: list[dict[str, Any]] = df.to_dict(orient="records")

        logger.debug("Successfully loaded %d records from Excel", len(transactions))
        return transactions

    except FileNotFoundError:
        logger.error("Excel file not found: %s", path)
        return []

    except Exception as error:
        logger.error("Error reading Excel file %s: %s", path, error)
        return []
