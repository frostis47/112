import json
import logging
import pandas as pd

logger = logging.getLogger("utils")
f_fo = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
logger.setLevel(logging.DEBUG)


def get_info_transactions(path_file: str) -> list[dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        with open(path_file, encoding="utf-8") as file:
            try:
                file_dict = json.load(file)
                logger.info("смотрим содержимое файла, формат list()")

                if type(file_dict) is not list:
                    logger.warning("файл не формата list()")
                    logger.info("Завершение работы")
                    return []

                logger.info("файл корректный, возвращаем содержимое")
                logger.info("Завершение работы")
                return file_dict

            except json.JSONDecodeError:
                logger.warning("файл не может быть прочитан, неверный формат")
                logger.info("Завершение работы")
                return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        logger.info("Завершение работы")
        return []


def get_info_transactions_csv(path_file: str) -> list[dict] | list:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        with open(path_file, encoding="utf-8") as file:
            try:
                file_dict = pd.read_csv(file, delimiter=";")
                logger.info("смотрим содержимое файла, формат pd.DataFrame")

                if type(file_dict) is not pd.DataFrame:
                    logger.warning("файл не формата pd.DataFrame")
                    logger.info("Завершение работы")
                    return []

                logger.info("файл корректный, возвращаем содержимое")
                logger.info("Завершение работы")
                return file_dict.to_dict(orient="records")
            except json.JSONDecodeError:
                logger.warning("файл не может быть прочитан, неверный формат")
                logger.info("Завершение работы")
                return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        logger.info("Завершение работы")
        return []


def get_info_transactions_xlsx(path_file: str) -> list[dict] | list:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        file_dict = pd.read_excel(path_file, index_col=0)
        logger.info("смотрим содержимое файла, формат pd.DataFrame")

        if type(file_dict) is not pd.DataFrame:
            logger.warning("файл не формата pd.DataFrame")
            logger.info("Завершение работы")
            return []

        logger.info("файл корректный, возвращаем содержимое")
        logger.info("Завершение работы")
        return file_dict.to_dict(orient="records")
    except json.JSONDecodeError:
        logger.warning("файл не может быть прочитан, неверный формат")
        logger.info("Завершение работы")
        return []

    except FileNotFoundError:
        logger.warning("файл не найден, неверный путь до файла")
        logger.info("Завершение работы")
        return []
