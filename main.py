from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

#Маскировка номера карты или счета
print(mask_account_card(input("Введите номер счета или тип и номер карты")))

#Преобразование даты
print(get_date("2024-03-11T02:26:18.671407"))

#Сортировка операций по статусу и времени
print(filter_by_state, sort_by_date)
