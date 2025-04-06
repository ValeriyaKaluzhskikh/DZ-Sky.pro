from datetime import datetime
from typing import Union

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


def get_date(my_date: Union[str]) -> Union[str]:
    """Функция конвертирования даты"""
    date_formats = [
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H",
        "%Y-%m-%dT",
        "%Y-%m",
        "%Y",
        "%H:%M:%S.%f",
        "%M:%S.%f",
        "%S.%f",
        "%f",
    ]
    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(my_date, fmt)
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError("Неверный формат даты")
