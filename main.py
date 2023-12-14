import os.path
from utils import utilits

operations_data_full_path = os.path.join('src', 'data', 'operations.json')

while True:
    if not os.path.isfile(operations_data_full_path):
        print("Файл с данными операций не найден!")
        break

    operations_list = utilits.load_data_ops(operations_data_full_path)

    sorted_list = sorted(operations_list, key=lambda x: x['date'], reverse=True)
    sorted_list = [d for d in sorted_list if d["state"] == "EXECUTED"]
    operations = sorted_list[:5]

    for operation in operations:
        print(utilits.show_operation(operation))

    break
