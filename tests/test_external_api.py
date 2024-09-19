from unittest.mock import patch

from src.external_api import all_amount_rub_convert

transaction = {
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
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}


@patch("requests.get")
def test_all_amount_rub(mock_get):
    mock_get.return_value.json.return_value = {'success': True, 'rates': {'RUB': 1.0}}
    assert all_amount_rub_convert(transaction) == 31957.58
