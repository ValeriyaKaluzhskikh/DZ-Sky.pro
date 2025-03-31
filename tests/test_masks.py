from typing import Any

import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card, mask", [("6831982470375048", "6831 98** **** 5048"), ("7000792289606361", "7000 79** **** 6361")]
)
def test_get_mask_card_number(card: Any, mask: Any) -> Any:
    """Тестирует верно введенные данные для карты"""
    assert get_mask_card_number(card) == mask


@pytest.mark.parametrize("account, mask", [("68319824703750489564", "**9564"), ("73654108430135874305", "**4305")])
def test_get_mask_account(account: Any, mask: Any) -> Any:
    """Тестирует верно введенные данные для счета"""
    assert get_mask_account(account) == mask


def test_error_get_mask() -> None:
    """Обрабатывает ошибку TypeError"""
    with pytest.raises(TypeError, match="Неверный формат!"):
        get_mask_card_number("")
        get_mask_account("1234")
