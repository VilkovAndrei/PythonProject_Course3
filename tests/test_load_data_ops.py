import os.path
from utils.utilits import load_data_ops


test_data_full_path = os.path.join('src', 'data', 'test_data.json')
test_result = [
  {
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
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]


def test_load_data_ops():
    assert load_data_ops(test_data_full_path) == test_result
