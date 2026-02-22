# Виджет банковских операций

## Цель проекта
Проект предназначен для обработки банковских операций клиента.

В рамках проекта реализованы функции для:
- маскирования номеров карт и счетов
- фильтрации операций по статусу
- сортировки операций по дате

Проект выполнен с соблюдением требований PEP 8, использованием линтеров и GitFlow.

---

## Установка

### Клонирование репозитория
git clone https://github.com/almsar99/homework_9.1.git
cd homework_9.1

---

## Зависимости и настройка окружения

Проект написан на Python 3.10+.
Для управления зависимостями используется Poetry.

### Установка Poetry
pip install poetry

### Установка зависимостей проекта
poetry install

### Активация виртуального окружения
poetry shell

---

## Проверка качества кода

Для проверки качества кода используются линтеры flake8 и mypy.

flake8 src
mypy src

---

## Использование

### Функция filter_by_state
Фильтрует список банковских операций по статусу.

from src.processing import filter_by_state

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]

filter_by_state(operations)
filter_by_state(operations, 'CANCELED')

---

### Функция sort_by_date
Сортирует список банковских операций по дате.

from src.processing import sort_by_date

sort_by_date(operations)
sort_by_date(operations, reverse=False)

---

## Разработка

Разработка ведётся по GitFlow:
- основная ветка — main
- новая функциональность разрабатывается в ветках feature/*
- изменения добавляются через Pull Request


---

## Модуль generators

В проект добавлен модуль `generators`, предназначенный для обработки транзакций
с использованием генераторов Python.  
Модуль позволяет эффективно работать с большими объёмами данных,
возвращая значения по запросу.

---

### filter_by_currency
Функция принимает список транзакций и код валюты.  
Возвращает итератор, который поочерёдно выдаёт транзакции,
у которых валюта операции соответствует заданной.

Пример использования:
```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions))
```

### transaction_descriptions
Генератор, который принимает список транзакций и возвращает описание каждой операции по очереди.

Пример использования:
```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)

for _ in range(3):
    print(next(descriptions))
```

### card_number_generator
Генератор, который выдаёт номера банковских карт
в формате 'XXXX XXXX XXXX XXXX'
в заданном диапазоне.

Пример использования:
```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
```
---

## Модуль decorators

В проект добавлен модуль `decorators`, содержащий декораторы
для логирования работы функций.

---

### Декоратор log

Декоратор `log` предназначен для логирования выполнения функций.

Возможности:
- логирование успешного выполнения функции
- логирование ошибок с указанием входных параметров
- вывод логов в консоль или запись в файл

#### Использование без файла (лог в консоль)

```python
from src.decorators import log

@log()
def add(a, b):
    return a + b

add(2, 3)
```

### Результат в консоли:
```text
add ok
```

### Использование с файлом
```python
from src.decorators import log

@log(filename="mylog.txt")
def div(a, b):
    return a / b

div(1, 0)
```

### Результат в файле mylog.txt:
```text
div error: division by zero. Inputs: (1, 0), {}
```

## Тестирование
Для тестирования проекта используется библиотека pytest.

Запуск всех тестов:
```bash
pytest
```
Запуск тестов с проверкой покрытия:
```bash
pytest --cov=src.decorators
```
Генерация HTML-отчёта покрытия:
```bash
pytest --cov=src.decorators --cov-report=html
```

HTML-отчёт покрытия сохраняется в директории htmlcov.

---

## Модуль readers

В проект добавлен модуль `readers`, реализующий считывание
финансовых операций из CSV и XLSX файлов
с использованием библиотеки pandas.

### load_transactions_from_csv(path: str)

Функция принимает путь к CSV-файлу и возвращает список словарей с транзакциями.

### load_transactions_from_excel(path: str)

Функция принимает путь к Excel-файлу и возвращает список словарей с транзакциями.
