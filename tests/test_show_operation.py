from utils.utilits import show_operation


test_dict_empty = {}
test_dict = {
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19T09:22:25.899614",
    "operationAmount": {
      "amount": "30153.72",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 7810846596785568",
    "to": "Счет 43241152692663622869"
  }

test_dict2 = {
    "id": 482520625,
    "state": "EXECUTED",
    "date": "2019-11-13T17:38:04.800051",
    "operationAmount": {
      "amount": "62814.53",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 38611439522855669794",
    "to": "Счет 46765464282437878125"
  }

test_dict3 = {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "to": "Visa Platinum 8990922113665229"
  }
def test_show_operation():
    assert show_operation(test_dict_empty) == ""
    assert show_operation(test_dict) == f"19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.\n"
    assert show_operation(test_dict2) == f"13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет **8125\n62814.53 руб.\n"
    assert show_operation(test_dict3) == f"19.08.2018 Перевод с карты на карту\n -> Visa Platinum 8990 92** **** 5229\n56883.54 USD\n"
