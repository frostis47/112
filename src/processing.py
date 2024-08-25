
def filter_by_state(infrom_states: list[dict[str, str | int]], state_id: str = "EXECUTED") -> list[dict[str, str | int]]:

    """Функция принимает на вход список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное в функцию
    значение."""
    list_stat = []
    for data in infrom_states:
        if data.get("state") == state_id:
            list_stat.append(data)
    return list_stat


print(filter_by_state)




def sort_by_date(infrom_states: list[dict[str, str | int]], reverse_list: bool = True) -> list[dict[str, str | int]]:
    """Функция, которая принимает список словарей и необязательный  порядок сортировки по умолчанию убывание"""
    sorted_infrom_state = sorted(infrom_states, key=lambda d: d['date'], reverse=reverse_list)
    return sorted_infrom_state

print(sort_by_date)



