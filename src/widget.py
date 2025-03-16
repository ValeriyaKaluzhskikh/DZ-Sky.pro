from typing import Union
from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_card: Union[str]) -> Union[str]:
    """Маскирует номер и карты, и счета"""
    account_card_split = account_card.split()
    if "Счет" in account_card_split:
        return f"Счет {get_mask_account(account_card_split[1])}"
    else:
        card_name = []
        card_numbers = []
        for i in account_card_split:
            if i.isdigit():
                card_numbers.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_name = " ".join(card_name)
        str_card_numbers = "".join(card_numbers)
        return f"{str_card_name} {get_mask_card_number(str_card_numbers)}"


def get_date(date_time: Union[str]) -> Union[str]:
    """Функция возвращает дату в формате ДД.ММ.ГГГГ"""
    date = date_time[:10]
    date_split = date.split("-")
    date_revers = date_split[::-1]
    final_date = ".".join(date_revers)
    return final_date