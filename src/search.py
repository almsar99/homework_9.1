import re
from typing import Any


def process_bank_search(
    data: list[dict[str, Any]], search: str
) -> list[dict[str, Any]]:
    """
    Ищет операции по строке в поле description
    с использованием регулярных выражений.
    """
    pattern = re.compile(search, re.IGNORECASE)

    return [
        operation
        for operation in data
        if pattern.search(str(operation.get("description", "")))
    ]


def process_bank_operations(
    data: list[dict[str, Any]], categories: list[str]
) -> dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям
    на основе поля description.
    """
    descriptions = [
        str(operation.get("description", ""))
        for operation in data
    ]

    result = {}

    for category in categories:
        pattern = re.compile(category, re.IGNORECASE)
        result[category] = sum(
            bool(pattern.search(description))
            for description in descriptions
        )

    return result
