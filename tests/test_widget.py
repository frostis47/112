import pytest


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_elements(n: str, expected_result: str) -> None:
    assert test_mask_elements(n) == expected_result


def test_get_date() -> None:
    assert test_get_date() == "11.07.2018"
