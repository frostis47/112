from src.funcional import find_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import (get_info_transactions, get_info_transactions_csv,
                       get_info_transactions_xlsx)
from src.widget import get_data, mask_account_card


def main() -> str:
    global result
    greeting = """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:\n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""

    input_user_file = input(f"{greeting}\n")

    while input_user_file not in ["1", "2", "3"]:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_file = input()

    # Получение данных в зависимости от выбранного формата файла
    if input_user_file == "1":
        print("\nДля обработки выбран JSON-файл.")
        result = get_info_transactions("data/operations.json")
    elif input_user_file == "2":
        print("\nДля обработки выбран CSV-файл.")
        result = get_info_transactions_csv("data/transactions.csv")
    elif input_user_file == "3":
        print("\nДля обработки выбран XLSX-файл.")
        result = get_info_transactions_xlsx("data/transactions_excel.xlsx")

    # Проверка, были ли загружены данные
    if not result:
        return "Не удалось загрузить транзакции."

    # Фильтрация по статусу
    ask_st = """\nВведите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    answer_user_state = input(f"{ask_st}\n").upper()

    while answer_user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"\nСтатус операции {answer_user_state} недоступен.\n{ask_st}")
        answer_user_state = input().upper()

    result = filter_by_state(result, answer_user_state)

    # Сортировка по дате
    next_choice_data = """\nОтсортировать операции по дате? Да/Нет"""
    input_user_data = input(f"{next_choice_data}\n").lower()
    while input_user_data not in ["да", "нет"]:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_data = input(f"{next_choice_data}\n").lower()

    if input_user_data == "да":
        next_choice_ascending = """\nОтсортировать по возрастанию или по убыванию?"""
        input_user_ascending = input(f"{next_choice_ascending}\n").lower()

        while input_user_ascending not in ["по возрастанию", "по убыванию"]:
            print("\nВвели некорректную сортировку\nПопробуйте еще раз:")
            input_user_ascending = input(f"{next_choice_ascending}\n").lower()

        result = sort_by_date(result, input_user_ascending == "по убыванию")

    # Фильтрация по валюте
    next_choice_rub = """\nВыводить только рублевые транзакции? Да/Нет"""
    input_user_rub = input(f"{next_choice_rub}\n").lower()
    while input_user_rub not in ["да", "нет"]:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_rub = input(f"{next_choice_rub}\n").lower()

    if input_user_rub == "да":
        result = list(filter_by_currency(result, "RUB"))

    # Фильтрация по слову в описании
    next_choice_word = """\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет"""
    input_user_word = input(f"{next_choice_word}\n").lower()
    while input_user_word not in ["да", "нет"]:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        input_user_word = input(f"{next_choice_word}\n").lower()

    if input_user_word == "да":
        word_filter = input("Введите слово для поиска:\n")
        result = find_transactions(result, word_filter)

    print("Распечатываю итоговый список транзакций...\n")

    # Проверка содержимого result перед обработкой
    if not result:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

    # Вывод информации о транзакциях
    for i in result:
        if isinstance(i, dict):
            data = get_data(i["date"])
            description = i["description"]
            from_ = mask_account_card(i.get("from", ""))
            to_ = mask_account_card(i.get("to", ""))
            amount = i["operationAmount"]["amount"]
            name = i["operationAmount"]["currency"]["name"]

            print(f"{data} {description}\n{from_} -> {to_}\nСумма: {amount} {name}\n")
        else:
            print(f"Неправильный тип данных в result: {i} (тип: {type(i)})")

    return "finish"


if __name__ == "__main__":
    main()
