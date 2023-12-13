from utils.utilits import hide_card_number


def test_hide_card_number():
    assert hide_card_number("1234567890123456") == "1234 56** **** 3456"


def test_hide_card_number_empty():
    assert hide_card_number("") == ""
