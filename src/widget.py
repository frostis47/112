def mask_account_card(card_number: str) -> str:
    """Функция для маскировки номера карты."""
    return "**** **** **** " + card_number[-4:]  # Пример маскировки

def mask_account_number(account_number: str) -> str:
    """Функция для маскировки номера счета."""
    return "****" + account_number[-4:]  # Пример маскировки

def masks_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты."""
    return "**** **** **** " + card_number[-4:]  # Пример маскировки

def mask_elements(element: str, mask=None) -> str | None:
    """Функция, маскирующая любой элемент,
    как номер карты, так и номер счёта"""
    if element[0] == "С":
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                masked_number = mask_account_number(element)  # Используем mask_account_number
                return f"Счет {masked_number}"

    else:
        for i in range(len(element)):
            if element[i].isalpha():
                continue
            elif element[i].isdigit():
                masked_card = masks_card_number(element)  # Используем masks_card_number
                return f"{element[:-16]}{masked_card}"
    return None

def get_date(date: str) -> str:
    """Функция получает дату из полученных данных и выводит её"""
    day, month, year = date[8:10], date[5:7], date[:4]
    return f'{day}.{month}.{year}'

def get_data(date: str) -> str:
    """Функция получает дату и возвращает её в нужном формате."""
    return get_date(date)  # Используем get_date для форматирования