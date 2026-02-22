from src.search import process_bank_operations, process_bank_search


def test_process_bank_search():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    result = process_bank_search(data, "перевод")

    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_process_bank_operations():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие счета"},
    ]

    categories = ["Перевод", "Открытие"]

    result = process_bank_operations(data, categories)

    assert result["Перевод"] == 2
    assert result["Открытие"] == 2


def test_process_bank_search_no_matches():
    data = [
        {"description": "Открытие вклада"},
        {"description": "Пополнение счета"},
    ]

    result = process_bank_search(data, "перевод")

    assert result == []


def test_process_bank_operations_no_matches():
    data = [
        {"description": "Открытие вклада"},
        {"description": "Пополнение счета"},
    ]

    categories = ["Перевод"]

    result = process_bank_operations(data, categories)

    assert result["Перевод"] == 0
