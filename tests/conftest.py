import pytest
from src.processing import old_list
from typing import Any


@pytest.fixture
def fixture_for_state() -> list[Any]:
    return old_list == [
        {"id": 41428829,
         "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"
         },
        {"id": 939719570,
         "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"
         },
        {"id": 54123123,
         "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"
         },
        {"id": 123123123,
         "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"
         },
    ]


@pytest.fixture
def info_transaction():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "code": "RUB"
                }
            }
        }
    ]


@pytest.fixture
def info_trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "code": "RUB"
            }
        }
    }


@pytest.fixture
def test_info_csv():
    return {'date': '2023-09-05T11:30:32Z',
            'description': 'Перевод организации',
            'from': 'Счет 58803664561298323391',
            'id': '650703',
            'operationAmount': {'amount': '16210',
                                'currency': {'code': 'PEN', 'name': 'Sol'}},
            'state': 'EXECUTED',
            'to': 'Счет 39745660563456619397'}


@pytest.fixture
def test_info_xlcx():
    return {'date': '2023-09-05T11:30:32Z',
            'description': 'Перевод организации',
            'from': 'Счет 58803664561298323391',
            'id': float(650703.0),
            'operationAmount': {'amount': float(16210.0),
                                'currency': {'code': 'PEN', 'name': 'Sol'}},
            'state': 'EXECUTED',
            'to': 'Счет 39745660563456619397'}
