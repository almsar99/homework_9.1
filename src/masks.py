def get_mask_card_number(number: str) -> str:
    """
    Преобразование номера карты в маску,
    :param number: данный параметр принимает тип данных в виде строки
    :return: строку в формате XXXX XX** **** XXXX
    """

    res_l = []
    count_stars = "*" * (len(number) - 10)
    split_number = f"{number[:6]}{count_stars}{number[-4:]}"
    for i in range(0, len(number), 4):
        res_l.append(split_number[i:i + 4])
    return " ".join(res_l)


def get_mask_account(number: str) -> str:
    """
    Преобразование номера в маску счета,
    :param number: данный параметр принимает тип данных в виде строки
    :return: строку в формате **XXXX
    """
    return f"**{number[-4:]}"