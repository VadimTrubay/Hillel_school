# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк

import pickle

data = [{
    'age': '30',
    'sex': 'Man',
    'city': 'Kiev'
    },
    {
     'age': '40',
     'sex': 'Woman',
     'city': 'Dnipro'
    },
    {
     'age': '50',
     'sex': 'Man',
     'city': 'Odessa'
    },
]

with open('my_file.txt', 'wb') as f:
    pickle.dump(data, f)

# with open('my_file.txt', 'rb') as f:
#     print(pickle.load(f))
