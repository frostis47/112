import json
import logging

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations_info(filename: str) -> list[dict]:
    """ Функция принимающая путь до файла и возвращающая python объект """
    try:
        logger.info(f'Производиться поиск файла для чтения')
        with open(filename, 'r', encoding='utf8') as f:
            data_info = json.load(f)
            if type(data_info) is not list:
                logger.error(f'Ошибка TypeError')
                return []
    except FileNotFoundError as ex:
        logger.error(f'Ошибка {ex}]')
        return []
    else:
        logger.info(f'Завершение работы')
        return data_info


if __name__ == '__main__':
    print(get_operations_info(filename='../data/operations.json'))
