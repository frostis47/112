import json
import logging
from typing import List, Dict

import pandas as pd

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(filename)s %(levelname)s: %(message)s")
logger = logging.getLogger("utils")


def get_info_transactions(path_file: str) -> List[Dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        with open(path_file, 'r', encoding="utf-8") as file:
            try:
                file_dict = json.load(file)
                logger.info("Смотрим содержимое файла, формат list()")

                if not isinstance(file_dict, list):
                    logger.warning("Файл не формата list()")
                    logger.info("Завершение работы")
                    return []

                logger.info("Файл корректный, возвращаем содержимое")
                return file_dict

            except json.JSONDecodeError:
                logger.warning("Файл не может быть прочитан, неверный формат")
                return []

    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []


def get_info_transactions_csv(path_file: str) -> List[Dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        df = pd.read_csv(path_file, delimiter=";")
        logger.info("Смотрим содержимое файла, формат pd.DataFrame")

        if not isinstance(df, pd.DataFrame):
            logger.warning("Файл не формата pd.DataFrame")
            return []

        logger.info("Файл корректный, возвращаем содержимое")
        return df.to_dict(orient="records")

    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []
    except Exception as e:
        logger.warning(f"Ошибка при чтении CSV файла: {e}")
        return []


def get_info_transactions_xlsx(path_file: str) -> List[Dict]:
    """
    Функция принимает путь до файла и возвращает операции в исходном файле
    в формате list[dict]
    """
    try:
        logger.info("Открываем файл...")

        df = pd.read_excel(path_file, index_col=0)
        logger.info("Смотрим содержимое файла, формат pd.DataFrame")

        if not isinstance(df, pd.DataFrame):
            logger.warning("Файл не формата pd.DataFrame")
            return []

        logger.info("Файл корректный, возвращаем содержимое")
        return df.to_dict(orient="records")

    except FileNotFoundError:
        logger.warning("Файл не найден, неверный путь до файла")
        return []
    except Exception as e:
        logger.warning(f"Ошибка при чтении XLSX файла: {e}")
        return []
