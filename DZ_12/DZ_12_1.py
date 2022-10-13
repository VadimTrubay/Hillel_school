# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей,
# а все значения представлены в виде строк

import pickle

a = [{'age': '30', 'sex': 'Man', 'city': 'Kiev'},
     {'age': '40', 'sex': 'Woman', 'city': 'Dnipro'},
     {'age': '50', 'sex': 'Man', 'city': 'Odessa'},
     ]

f = open('my_file.bin', 'wb')
pickle.dump(a, f)
f.close()

f = open('my_file.bin', 'rb')
b = pickle.load(f)
print('b = ', b)
f.close()
