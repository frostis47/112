import pytest
from unittest.mock import patch
from src.utils import financial_transactions, transaction_amount

@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

def test_financial_transactions_nofile():
    assert financial_transactions('nofile') == []

def test_financial_transactions(path):
    expected_transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    assert financial_transactions(path)[0] == expected_transaction

def test_financial_transactions_empty_list(path_empty_list):
    assert financial_transactions(path_empty_list) == []

def test_financial_transactions_mistake_json(path_mistake_json):
    assert financial_transactions(path_mistake_json) == []

def test_transaction_amount(trans):
    assert transaction_amount(trans) == '31957.58'

@patch('src.utils.currency_conversion')
def test_transaction_amount_non_rub(mock_currency_conversion, trans):
    mock_currency_conversion.return_value = 1000.0
    assert transaction_amount(trans) == 1000.0