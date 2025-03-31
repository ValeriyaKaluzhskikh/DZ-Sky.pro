from typing import Any

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_1(test_dict: Any) -> Any:
    """Тест с обычным словарем"""
    assert filter_by_state(test_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_2(test_dict: Any) -> Any:
    """Тест на изменение значения"""
    assert filter_by_state(test_dict, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_3(test_dict: Any) -> Any:
    """Тест на ошибку в значении"""
    assert filter_by_state(test_dict, state="CANCELES") == []


def test_filter_by_state_4() -> None:
    """Тест на передачу пустого словаря"""
    assert filter_by_state([]) == []


def test_sort_by_date_1(test_dict: Any) -> Any:
    """Тест с обычным словарем"""
    assert sort_by_date(test_dict) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


def test_sort_by_date_2(test_dict: Any) -> Any:
    """Тест на изменение значения"""
    assert sort_by_date(test_dict, flow=False) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


def test_sort_by_date_3() -> None:
    """Тест на передачу пустого словаря"""
    assert sort_by_date([]) == []
