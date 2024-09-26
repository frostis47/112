import pytest
from src.generators import transactions, filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency():
    # Проверяем, что фильтрация по валюте RUB возвращает правильные транзакции
    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 2  # Ожидаем 2 транзакции
    assert rub_transactions[0]["id"] == 873106923
    assert rub_transactions[1]["id"] == 594226727

    # Проверяем, что фильтрация по валюте USD возвращает правильные транзакции
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 3  # Ожидаем 3 транзакции
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268
    assert usd_transactions[2]["id"] == 895315941

def test_transaction_descriptions():
    # Проверяем, что описания транзакций возвращаются правильно
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 5  # Ожидаем 5 описаний
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Перевод со счета на счет"
    assert descriptions[2] == "Перевод со счета на счет"
    assert descriptions[3] == "Перевод с карты на карту"
    assert descriptions[4] == "Перевод организации"

def test_card_number_generator():
    # Проверяем, что генератор карт работает правильно
    generated_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert generated_numbers == expected_numbers