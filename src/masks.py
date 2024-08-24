def get_mask_card_number(card_number: str) -> str:

    """Функцию маскировки номера банковской карты"""
    return f"{card_number[:4]} {card_number[2:4]}{"*" * 2} {"*" * 4} {card_number[12:]}"


def get_mask_account(score_number: str):
    """Функцию маскировки номера банковского счета """
    return f"{"*" * 2} {score_number[16:]}"












