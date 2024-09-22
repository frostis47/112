import os
import logging
import json
import pandas as pd

log_directory = '../logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

file_handler = logging.FileHandler(os.path.join(log_directory, 'utils.log'), encoding='utf-8')
logging.basicConfig(level=logging.INFO, handlers=[file_handler])

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
        logger.error(f'Ошибка {ex}')
        return []
    except json.JSONDecodeError as ex:
        logger.error(f'Ошибка JSON: {ex}')
        return []
    else:
        logger.info(f'Завершение работы')
        return data_info


def get_info_transactions():
    pass


def get_info_transactions_csv(filename: str) -> list[dict]:
    """ Функция для чтения данных из CSV файла и возвращения их в виде списка словарей.
    @rtype: object
    """
    try:
        logger.info(f'Чтение данных из файла {filename}')
        data_info = pd.read_csv(filename).to_dict(orient='records')
        return data_info
    except FileNotFoundError as ex:
        logger.error(f'Ошибка {ex}')
        return []
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла: {ex}')
        return []


def get_info_transactions_xlsx(filename: str) -> list[dict]:
    """ Функция для чтения данных из XLSX файла и возвращения их в виде списка словарей. """
    try:
        logger.info(f'Чтение данных из файла {filename}')
        data_info = pd.read_excel(filename).to_dict(orient='records')
        return data_info
    except FileNotFoundError as ex:
        logger.error(f'Ошибка {ex}')
        return []
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла: {ex}')
        return []


if __name__ == '__main__':
    print(get_operations_info(filename='../data/operations.json'))


    def get_info_transactions():
        pass
