def filter_by_state(operations: list, state: str="EXECUTED") -> list:
    """Функция фильтрует операции в списке по ключу 'state'"""
    list_of_operation = []
    for item in operations:
        if item["state"] == state:
            list_of_operation.append(item)
    return list_of_operation


def sort_by_date(operations: list, flow: bool = True) -> list:
    """Функция сортирует операции по дате"""
    sort_by_date_list = sorted(operations, key=lambda item: item["date"], reverse=flow)
    return sort_by_date_list

