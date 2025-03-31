from src.processing import filter_by_state
from src.processing import sort_by_date
from src.widget import get_date
from src.widget import mask_account_card

# Маскировка номера карты или счета
print(mask_account_card(input("Введите номер счета или тип и номер карты")))

# Преобразование даты
print(get_date(input("Текущее время")))


# Сортировка операций по статусу
print(filter_by_state())

# Сортировка операций по времени
print(sort_by_date())
