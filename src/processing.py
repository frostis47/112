from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
Функция фильтрует данные по указанному состоянию список словарей с данными состояние,
по которому необходимо отфильтровать данные (по умолчанию 'EXECUTED')
    """
    return [d for d in data if d.get('state') == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Return filtered list by date"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list


old_list = [
    {"id": 41428829,
     "state": "EXECUTED",
     "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570,
     "state": "EXECUTED",
     "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727,
     "state": "CANCELED",
     "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591,
     "state": "CANCELED",
     "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(old_list: list, state: str = "EXECUTED") -> list[str]:
    """Функция, получает список словарей и возвращает новый список."""
    new_list = []
    new_list_for_canceled = []
    for i in old_list:
        if i.get("state") == state:
            new_list.append(i)
        else:
            new_list_for_canceled.append(i)
    return new_list


def sort_by_date(old_list: list, is_date: bool = True) -> list[str]:
    """Функция, Которая возвращает список по убыванию."""
    sort_old_list = sorted(old_list, key=lambda x: x["date"], reverse=is_date)
    return sort_old_list


if __name__ == '__main__':
    filter_by_state(old_list, state="EXECUTED")
    sort_by_date(old_list)
