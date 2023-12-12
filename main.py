import os.path
from datetime import datetime
import utilits
from operator import itemgetter


# data_path = 'src\data'
operations_data_full_path = os.path.join('src', 'data', 'operations.json')
print(operations_data_full_path)
while True:
    if not os.path.isfile(operations_data_full_path):
        print("Файл с данными операций не найден!")
        break
    break

operations_list = utilits.load_data_ops(operations_data_full_path)

sorted_list = sorted(operations_list, key=lambda x: x['date'], reverse=True)
sorted_list = [d for d in sorted_list if d["state"]=="EXECUTED"]
operations = sorted_list[:5]
