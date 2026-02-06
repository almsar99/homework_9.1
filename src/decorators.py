from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: имя файла для записи логов.
                     Если None — лог выводится в консоль.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as error:
                message = (
                    f"{func.__name__} error: {error}. "
                    f"Inputs: {args}, {kwargs}"
                )
                _write_log(message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
