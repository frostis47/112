import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(num: str) -> str:
    """ Функция принимает номер карты и возвращает замаскированный номер
    @rtype: object """
    logger.info(f"start masked_card_num {num}")
    number = 4
    result = num[:number] + " " + num[number: number + 2] + "** ****" + " " + num[number + 8:]
    logger.info(f"mask {result}")
    return result


if __name__ == '__main__':
    print(get_mask_card_number("8990922113665229"))


def get_mask_account_number(num: str) -> str:
    """ Функция принимает номер счёта и возвращает замаскированный номер """
    logger.info(f"start masked_account_num {num}")
    result = "**" + num[-4:]
    logger.info(f"mask {result}")
    return result


if __name__ == '__main__':
    print(get_mask_account_number("73654108430135874305"))