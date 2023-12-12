import json


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
