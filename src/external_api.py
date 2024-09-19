import os
import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv()

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


def all_amount_rub_convert(transaction: Any) -> float:
    """Функция возвращает сумму транзакции в рублях."""
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return amount


        API_KEY = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        if 'rates' in data and 'RUB' in data['rates']:
            exchange_rate = data['rates']['RUB']
            return amount * exchange_rate

        print(f"Курс для валюты {currency} не найден")
        return 0.0

    except (KeyError, TypeError, ValueError, requests.RequestException) as e:
        print(f"Error: {e}")
        return 0.0


if __name__ == '__main__':
    print(all_amount_rub_convert(transaction))