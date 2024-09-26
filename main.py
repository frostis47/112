from src.funcional import find_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import (get_info_transactions, get_info_transactions_csv,
                       get_info_transactions_xlsx)
from src.widget import get_data, mask_account_card


def get_user_input(prompt, valid_options):
    """Функция для получения корректного ввода от пользователя."""
    user_input = input(prompt).strip()
    while user_input not in valid_options:
        print("\nВвели некорректный символ\nПопробуйте еще раз:")
        user_input = input(prompt).strip()
    return user_input


def load_transactions(input_user_file):
    """Загрузка транзакций в зависимости от выбранного формата файла."""
    file_map = {
        "1": ("data/operations.json", get_info_transactions),
        "2": ("data/transactions.csv", get_info_transactions_csv),
        "3": ("data/transactions_excel.xlsx", get_info_transactions_xlsx)
    }
    file_name, load_function = file_map[input_user_file]
    print(f"\nДля обработки выбран {['JSON', 'CSV', 'XLSX'][int(input_user_file) - 1]}-файл.")
    return load_function(file_name)


def main() -> str:
    greeting = """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:\n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""

    input_user_file = get_user_input(f"{greeting}\n", ["1", "2", "3"])
    result = load_transactions(input_user_file)

    if not result:
        return "Не удалось загрузить транзакции."

    # Фильтрация по статусу
    answer_user_state = get_user_input(
        "\nВведите статус для фильтрации (EXECUTED, CANCELED, PENDING):\n",
        ["EXECUTED", "CANCELED", "PENDING"]
    )
    result = filter_by_state(result, answer_user_state)

    # Сортировка по дате
    if get_user_input("\nОтсортировать операции по дате? Да/Нет\n", ["да", "нет"]) == "да":
        order = get_user_input("\nОтсортировать по возрастанию или по убыванию?\n", ["по возрастанию", "по убыванию"])
        result = sort_by_date(result, order == "по убыванию")

    # Фильтрация по валюте
    if get_user_input("\nВыводить только рублевые транзакции? Да/Нет\n", ["да", "нет"]) == "да":
        result = list(filter_by_currency(result, "RUB"))

    # Фильтрация по слову в описании
    if get_user_input("\nОтфильтровать список транзакций по слову в описании? Да/Нет\n", ["да", "нет"]) == "да":
        word_filter = input("Введите слово для поиска:\n")
        result = find_transactions(result, word_filter)

    print("Распечатываю итоговый список транзакций...\n")

    if not result:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


    # Вывод информации о транзакциях
    for i in result:
        if isinstance(i, dict):
            data = get_data(i["date"])  # Это должно работать, если get_data принимает date
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