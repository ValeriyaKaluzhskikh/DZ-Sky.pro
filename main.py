from src.processing import filter_by_state
from src.processing import sort_by_date
from src.widget import get_date
from src.widget import mask_account_card

# Маскировка номера карты или счета
print(mask_account_card(input("Введите номер счета или тип и номер карты")))

# Преобразование даты
print(get_date(input("Текущее время")))


dictionary_example = (
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
)
# Сортировка операций по статусу
print(filter_by_state(dictionary_example))

# Сортировка операций по времени
print(sort_by_date(dictionary_example))
