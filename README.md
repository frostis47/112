# Домашнее задание

## Описание

Функция "filter_by_state", которая принимает список слов и опциональное значение для включения "состояния". Функция возвращает новый список слов, включающий только те словари, в которых ключ «state» соответствует заданному результату.

## Установка
Скачать Pycharm

Клонируйте репозитории:

git@github.com:frostis47/112.git

## Использование:

Перейти на страницу в вашем браузере.

Сделайте учетную запись или введите новое значение в Github.

## Тестирование
1. Модуль маски 1.1 Функция get_mask_card_number
1.2 Тестирование правильности маскировки номеров карт. 
1.3 def test_get_mask_card_number() -> Нет: Assert get_mask_card_number("7000799978996361") == "7000 79** **** 6361" 

2. функция get_mask_account 
2.1 Тестирование правильности маскировки номера счета. 
2.2 def test_get_mask_account() -> Нет: утверждать get_mask_account_number("98766667774305") == "**4305"

3. Модуль виджета 
3.1 функция Mask_account_card 
3.2 Тесты для проверки, которые корректно распознают и применяют нужный тип маскировки в зависимости от типа входных данных (карта или счет). 
3.3 def test_mask_elements(n: str, ожидаемый_результат: str) -> Нет: утверждать test_mask_elements(n) == ожидаемый_результат 
3.4 функция get_data 
3.5 Тестирование правильно преобразовать дату. 
3.6 def test_get_date() -> Нет: Assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"

4. Модуль обработки 
4.1 Функция filter_by_state 
4.2 Тестирование фильтрации списка слов по заданному статусу state . 
4.3 def test_filter_by_state(n, ожидаемый): Assert filter_by_state(n) == ожидаемый 
4.4 функция sort_by_date 
4.5 Тестирование сортировки словарных слов по датам в порядке убывания и возрастания. 
4.6 def test_sort_by_date(n, ожидается): Assert sort_by_date(n) == ожидается

5. Модуль-генераторы 
5.1 Создает функцию filter_by_currency, которая принимает во входной список словерей, предоставляющих транзакции. 
5.2 def test_filter_by_currency(): Assert next(filter_by_currency(transactions, "RUB")) == 873106923 
5.3 Генератор транзакций оторый принимает список словерей с транзакциями и возвращает описание каждой операции по очереди. 
5.4 def test_transaction_descriptions(): Assert next(transaction_descriptions(transactions)) == "Перевод организации" 
5.5 Генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX 
5.6 def test_card_number_generator(): Assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"

6. Произведено тестирование для модуля external_api.py
   с помошью "mock и path"
def all_amount_rub_convert(transaction: Any) -> float:
6.1 Произведено тестирование модуля untils.py
def get_info_json_object(capsys):
def test_info_json_emty(capsys):