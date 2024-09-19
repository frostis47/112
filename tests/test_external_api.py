from unittest.mock import patch
import pytest
from src.external_api import currency_conversion


@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "���.",
                "code": "USD"
            }
        },
        "description": "������� �����������",
        "from": "Maestro 1596837868705199",
        "to": "���� 64686473678894779589"
    }


@patch('src.external_api.requests.get')
def test_currency_conversion(mock_get, trans):
    mock_get.return_value.json.return_value = {
        'success': True,
        'query': {
            'from': 'USD',
            'to': 'RUB',
            'amount': 8221.37
        },
        'info': {
            'timestamp': 1724671757,
            'rate': 91.475458
        },
        'date': '2024-08-26',
        'result': 752053.586137
    }
    result = currency_conversion(trans)
    assert result == 752053.586137
