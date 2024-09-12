# Домашнее задание
## Описание 

Функция "filter_by_state" которая принимает список словарей и опционально значение для ключа "state".
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
"state" соответствует указанному значению.


## Установка 


1. Скачать Pycharm

2. Клонируйте репозиторий:

``git@github.com:frostis47/112.git``


## Использование:

1. Перейти на страницу в вашем браузере.
2. Создайте новую учетную запись или войдите существующей в Github.


## Тестирование 
1. Модуль masks 
1.1 Функция get_mask_card_number
1.2 Тестирование правильности маскирования номера карты.
1.3 def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000799978996361") == "7000 79** **** 6361"
2 Функция get_mask_account
2.1 Тестирование правильности маскирования номера счета.
2.2 def test_get_mask_account() -> None:
    assert get_mask_account_number("98766667774305") == "**4305"
3. Модуль widget
3.1 Функция mask_account_card 
3.2 Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
3.3 def test_mask_elements(n: str, expected_result: str) -> None:
    assert test_mask_elements(n) == expected_result
3.4 Функция get_data
3.5 Тестирование правильности преобразования даты.
3.6 def test_get_date() -> None:
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
4. Модуль processing
4.1 Функция filter_by_state
4.2 Тестирование фильтрации списка словарей по заданному статусу 
state .
4.3 def test_filter_by_state(n, expected):
    assert filter_by_state(n) == expected
4.4 Функция sort_by_date
4.5 Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
4.6 def test_sort_by_date(n, expected):
    assert sort_by_date(n) == expected
5.  Модуль generators
5.1 Создает функцию 
filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.
5.2 def test_filter_by_currency():
    assert next(filter_by_currency(transactions, "RUB")) == 873106923
5.3 Генератор 
transaction_descriptions оторый принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
5.4 def test_transaction_descriptions():
    assert next(transaction_descriptions(transactions)) == "Перевод организации"
5.5 Генератор 
card_number_generator который выдает номера банковских карт в формате 
XXXX XXXX XXXX XXXX
5.6 def test_card_number_generator():
    assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"