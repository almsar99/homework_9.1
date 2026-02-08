import logging
from pathlib import Path

# --- logger setup ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_DIR / "masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """
    Преобразование номера карты в маску,
    :param number: данный параметр принимает тип данных в виде строки
    :return: строку в формате XXXX XX** **** XXXX
    """
    logger.debug(f"Masking card number: {number}")

    try:
        res_l = []
        count_stars = "*" * (len(number) - 10)
        split_number = f"{number[:6]}{count_stars}{number[-4:]}"

        for i in range(0, len(number), 4):
            res_l.append(split_number[i:i + 4])

        result = " ".join(res_l)
        logger.debug(f"Card number masked successfully: {result}")
        return result

    except Exception as error:
        logger.error(f"Error masking card number {number}: {error}")
        raise


def get_mask_account(number: str) -> str:
    """
    Преобразование номера в маску счета,
    :param number: данный параметр принимает тип данных в виде строки
    :return: строку в формате **XXXX
    """
    logger.debug(f"Masking account number: {number}")

    try:
        result = f"**{number[-4:]}"
        logger.debug(f"Account number masked successfully: {result}")
        return result

    except Exception as error:
        logger.error(f"Error masking account number {number}: {error}")
        raise
