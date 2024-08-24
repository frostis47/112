from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция общей маскировки карты и счета """

    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
        return result


print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 35383033474447895560"))


def get_data(date: str) -> str:
    """Функция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_data("2024-03-11T02:26:18.671407"))


