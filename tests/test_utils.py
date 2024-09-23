from unittest.mock import patch, mock_open

from src.utils import get_info_transactions


def test_get_info_transactions(info_transaction):
    assert get_info_transactions(1) == []
    assert get_info_transactions("") == []


@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_get_info_transactions_csv_xlsx(mock_file):
    assert open("../Data/test_transactions.csv").read() == "data"
    mock_file.assert_called_with("../Data/test_transactions.csv")

    assert open("../Data/transactions_excel.xlsx").read() == "data"
    mock_file.assert_called_with("../Data/transactions_excel.xlsx")
