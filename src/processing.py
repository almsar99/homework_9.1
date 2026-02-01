from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]],
    state: str = 'EXECUTED',
) -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по статусу.

    :param operations: список словарей с операциями
    :param state: статус операции (по умолчанию 'EXECUTED')
    :return: новый список операций с указанным статусом
    """
    return [
        operation
        for operation in operations
        if operation.get('state') == state
    ]


def sort_by_date(
    operations: List[Dict[str, Any]],
    reverse: bool = True,
) -> List[Dict[str, Any]]:
    """
    Сортирует банковские операции по дате.

    :param operations: список словарей с операциями
    :param reverse: порядок сортировки (по умолчанию убывание)
    :return: новый отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda operation: operation.get('date', ''),
        reverse=reverse,
    )