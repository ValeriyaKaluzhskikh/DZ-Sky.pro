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


def test_error_mask_account_card() -> None:
    """Обрабатывает ошибку TypeError"""
    with pytest.raises(TypeError, match="Неверный формат!"):
        mask_account_card("")


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


@pytest.mark.parametrize(
    "data, result",
    [
        ("2024-13-11T02:26:18.671407", "Неверный формат даты"),
        ("2453748674345", "Неверный формат даты"),
        (" ", "Неверный формат даты"),
    ],
)
def test_error_get_date(data: Any, result: Any) -> Any:
    """Обрабатывает ошибку ValueError"""
    with pytest.raises(ValueError, match=result):
        get_date(data)
