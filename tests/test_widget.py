from typing import Any

import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "card, mask",
    [
        ("6831982470375048", " 6831 98** **** 5048"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card: Any, mask: Any) -> Any:
    """Тестирует верно введенные данные для карты и счета"""
    assert mask_account_card(card) == mask


@pytest.mark.parametrize(
    "data, result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-01-31T11:30:21.514894", "31.01.2025"),
        ("2010-12-01T13:01:09.458247", "01.12.2010"),
    ],
)
def test_get_date(data: Any, result: Any) -> Any:
    """Тестирует верно введенные данные для времени"""
    assert get_date(data) == result


def test_get_date_with_invalid_date_string(invalid_date_string: str) -> None:
    """Тест для функции преобразования даты - несуществующая дата"""
    assert get_date(invalid_date_string) == "Проверьте правильность ввода!"


def test_get_date_with_another_invalid_date_string(another_invalid_date_string: str) -> None:
    """Тест для функции преобразования даты - строка, не преобразуемая в дату"""
    assert get_date(another_invalid_date_string) == "Проверьте правильность ввода!"


def test_get_date_with_empty_date_string(empty_date_string: str) -> None:
    """Тест для функции преобразования даты - пустая строка"""
    assert get_date(empty_date_string) == "Проверьте правильность ввода!"
