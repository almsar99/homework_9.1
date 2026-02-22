from datetime import datetime
from typing import Any

from src.readers import load_transactions_from_csv, load_transactions_from_excel
from src.search import process_bank_search
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def choose_file() -> list[dict[str, Any]]:
    """
    Выбор источника данных.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Введите номер пункта: ")

        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            return load_transactions("data/operations.json")

        if choice == "2":
            print("Для обработки выбран CSV-файл.")
            return load_transactions_from_csv("data/transactions.csv")

        if choice == "3":
            print("Для обработки выбран XLSX-файл.")
            return load_transactions_from_excel("data/transactions_excel.xlsx")

        print("Некорректный ввод. Попробуйте снова.")


def filter_by_status(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Фильтрация по статусу.
    """
    available_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input(
            "Введите статус (EXECUTED, CANCELED, PENDING): "
        ).upper()

        if status not in available_statuses:
            print(f'Статус операции "{status}" недоступен.')
            continue

        print(f'Операции отфильтрованы по статусу "{status}"')

        return [
            operation
            for operation in data
            if operation.get("state", "").upper() == status
        ]


def sort_by_date(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Сортировка операций по дате.
    """
    choice = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if choice != "да":
        return data

    order = input("По возрастанию или по убыванию? ").lower()
    reverse = order == "по убыванию"

    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x.get("date", "")),
        reverse=reverse,
    )


def filter_only_rub(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Фильтр только рублевых операций.
    """
    choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()

    if choice != "да":
        return data

    return [
        operation
        for operation in data
        if operation.get("operationAmount", {})
        .get("currency", {})
        .get("code") == "RUB"
    ]


def format_operation(operation: dict[str, Any]) -> None:
    """
    Красивый вывод операции.
    """
    date = get_date(operation.get("date", ""))
    description = operation.get("description", "")

    print(f"{date} {description}")

    from_account = operation.get("from")
    to_account = operation.get("to")

    if from_account:
        print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
    else:
        print(mask_account_card(to_account))

    amount = operation.get("operationAmount", {})
    value = amount.get("amount")
    currency = amount.get("currency", {}).get("code")

    print(f"Сумма: {value} {currency}\n")


def main() -> None:
    """
    Основная функция программы.
    """
    data = choose_file()
    data = filter_by_status(data)
    data = sort_by_date(data)
    data = filter_only_rub(data)

    search_choice = input(
        "Отфильтровать список транзакций по слову в описании? Да/Нет: "
    ).lower()

    if search_choice == "да":
        word = input("Введите слово для поиска: ")
        data = process_bank_search(data, word)

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия.")
        return

    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(data)}\n")

    for operation in data:
        format_operation(operation)


if __name__ == "__main__":
    main()
