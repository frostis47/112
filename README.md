# �������� �������

## ��������

������� "filter_by_state", ������� ��������� ������ ���� � ������������ �������� ��� ��������� "���������". ������� ���������� ����� ������ ����, ���������� ������ �� �������, � ������� ���� �state� ������������� ��������� ����������.

## ���������
������� Pycharm

���������� �����������:

git@github.com:frostis47/112.git

## �������������:

������� �� �������� � ����� ��������.

�������� ������� ������ ��� ������� ����� �������� � Github.

## ������������
1. ������ ����� 1.1 ������� get_mask_card_number
1.2 ������������ ������������ ���������� ������� ����. 
1.3 def test_get_mask_card_number() -> ���: Assert get_mask_card_number("7000799978996361") == "7000 79** **** 6361" 

2. ������� get_mask_account 
2.1 ������������ ������������ ���������� ������ �����. 
2.2 def test_get_mask_account() -> ���: ���������� get_mask_account_number("98766667774305") == "**4305"

3. ������ ������� 
3.1 ������� Mask_account_card 
3.2 ����� ��� ��������, ������� ��������� ���������� � ��������� ������ ��� ���������� � ����������� �� ���� ������� ������ (����� ��� ����). 
3.3 def test_mask_elements(n: str, ���������_���������: str) -> ���: ���������� test_mask_elements(n) == ���������_��������� 
3.4 ������� get_data 
3.5 ������������ ��������� ������������� ����. 
3.6 def test_get_date() -> ���: Assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"

4. ������ ��������� 
4.1 ������� filter_by_state 
4.2 ������������ ���������� ������ ���� �� ��������� ������� state . 
4.3 def test_filter_by_state(n, ���������): Assert filter_by_state(n) == ��������� 
4.4 ������� sort_by_date 
4.5 ������������ ���������� ��������� ���� �� ����� � ������� �������� � �����������. 
4.6 def test_sort_by_date(n, ���������): Assert sort_by_date(n) == ���������

5. ������-���������� 
5.1 ������� ������� filter_by_currency, ������� ��������� �� ������� ������ ��������, ��������������� ����������. 
5.2 def test_filter_by_currency(): Assert next(filter_by_currency(transactions, "RUB")) == 873106923 
5.3 ��������� ���������� ������ ��������� ������ �������� � ������������ � ���������� �������� ������ �������� �� �������. 
5.4 def test_transaction_descriptions(): Assert next(transaction_descriptions(transactions)) == "������� �����������" 
5.5 ��������� card_number_generator, ������� ������ ������ ���������� ���� � ������� XXXX XXXX XXXX XXXX 
5.6 def test_card_number_generator(): Assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"

6. ����������� ������������ ��� ������ external_api.py
   � ������� "mock � path"
def all_amount_rub_convert(transaction: Any) -> float:
6.1 ����������� ������������ ������ untils.py
def get_info_json_object(capsys):
def test_info_json_emty(capsys):