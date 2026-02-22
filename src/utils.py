import json
import logging
from pathlib import Path
from typing import Any

# --- logger setup ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_DIR / "utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_transactions(path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param path: путь к JSON-файлу
    :return: список словарей с транзакциями
    """
    try:
        logger.debug("Attempting to load transactions from %s", path)

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.error(
                "Invalid JSON structure in %s: expected list, got %s",
                path,
                type(data),
            )
            return []

        logger.debug("Successfully loaded %d transactions", len(data))
        return data

    except FileNotFoundError:
        logger.error("File not found: %s", path)
        return []

    except json.JSONDecodeError as error:
        logger.error("JSON decode error in %s: %s", path, error)
        return []
