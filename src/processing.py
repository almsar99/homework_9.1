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