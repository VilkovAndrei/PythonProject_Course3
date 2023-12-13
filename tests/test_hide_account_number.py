from utilits import hide_account_number


def test_hide_account_number():
    assert hide_account_number("12345678901234567890") == "**7890"


def test_hide_card_number_empty():
    assert hide_account_number("") == ""
