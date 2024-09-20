from src import masks


def mask_account_number():
    pass


def masks_card_number():
    pass


def mask_elements(element: str, mask=None) -> str | None:
    """Функция, маскирующая любой элемент,
    как номер карты, так и номер счёта"""
    if element[0] == "С":
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                mask_account_number()
                return f"Счет {masks}"

    else:
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                masks_card_number()
                return f"{element[:-16]}{mask}"
    return None


def get_date(date: str) -> str:
    """Функция получает дату из полученных данных и выводит её"""
    day, month, year = date[8:10], date[5:7], date[:4]
    return f'{day}.{month}.{year}'
