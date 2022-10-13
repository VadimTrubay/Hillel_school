# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей,
# а все значения представлены в виде строк

import pickle

a = [{'age': '30', 'sex': 'Man', 'city': 'Od'},
     {'age': '40', 'sex': 'Mann', 'city': 'Ode'},
     {'age': '50', 'sex': 'Mannn', 'city': 'Odess'},
]

f = open('myfile.bin', 'wb')
pickle.dump(a, f)
f.close()

f = open('myfile.bin', 'rb')
b = pickle.load(f)
print('b = ', b)
f.close()