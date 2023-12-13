import json
from datetime import date


def load_data_ops(file_name):
    """
    Загружает список операций из файла
    :param file_name: имя файла
    :return:
    """
    with open(file_name, mode='r', encoding='utf-8') as file:
        operations = json.load(file)

    operations = [d for d in operations if d != {}]  # очистка от пустых словарей

    return operations


def show_operation(operation_dict):
    """
    Вывод на экран информации по банковской операции
    :param operation_dict:
    :return:
    """
    op_date = date.fromisoformat(operation_dict['date'][:10]).strftime("%d.%m.%Y")
    operation_description = operation_dict["description"]
    if "from" not in operation_dict.keys():
        operation_from = ""
    else:
        if operation_dict["from"][:5] == "Счет ":
            operation_from = "Счет " + hide_account_number(operation_dict["from"])
        else:
            operation_from = operation_dict["from"][:-16] + hide_card_number(operation_dict["from"])

    if operation_dict["to"][:5] == "Счет ":
        operation_to = "Счет " + hide_account_number(operation_dict["to"])
    else:
        operation_to = operation_dict["to"][:-16] + hide_card_number(operation_dict["to"])

    op_amount = operation_dict["operationAmount"]["amount"]
    op_currency = operation_dict["operationAmount"]["currency"]["name"]

    return print(f"{op_date} {operation_description}\n{operation_from} -> {operation_to}\n{op_amount} {op_currency}\n")


def hide_card_number(operation_card_number):
    """
    Скрывает часть номера карты
    :param operation_card_number:
    :return:
    """
    if operation_card_number != '':
        card_number = operation_card_number[-16:]
        h_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        h_card_number = ''

    return h_card_number


def hide_account_number(operation_account_number):
    """
    Скрывает часть номера счета
    :param operation_account_number:
    :return:
    """
    if operation_account_number != '':
        account_number = operation_account_number[-20:]
        h_account_number = "**" + account_number[-4:]
    else:
        h_account_number = ''

    return h_account_number
