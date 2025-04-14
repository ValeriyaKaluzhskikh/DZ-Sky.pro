from datetime import datetime
from typing import Union

from src.decorators import log
from src.masks import get_mask_account
from src.masks import get_mask_card_number


@log()
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


@log()
def get_date(input_date: str) -> str:
    """Функция переводит дату в формат ДД.ММ.ГГГГ"""
    try:
        formated_date = datetime.strptime(input_date[:10], "%Y-%m-%d")
        return f"{formated_date.day:02}.{formated_date.month:02}.{formated_date.year}"
    except ValueError:
        return "Проверьте правильность ввода!"
