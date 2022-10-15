# Дано два словаря
# A = {'key': 1}
# B = {'key1: 2}
# Необходимо написать код который будет их объединять
# C = {'key': 1, 'key1': 2}
# Но нужно так-же учитывать коллизии,
# например ситуация когда у нас два одинаковых ключа и
# чтобы не потерять значения нужно записать в один ключ список
# в котором будут находится значения
# Например:
# A = {'key': 1, 'key2': True}
# B = {'key': 'Hello'}
# C = {'key': [1, 'Hello'], 'key2': True}
# Записать результат в файл result.json в формате JSON.

import json

A = {'key': 1, 'key1': True}
B = {'key': 'Hello', 'key1': False, 'key2': 'word'}
C = dict.copy(A)
for key, value in B.items():
    if C.get(key):
        C[key] = [C[key], value]
    else:
        C[key] = value

with open('result.json', 'w') as f:
    json.dump(C, f)

with open('result.json', 'r') as f:
    print(json.load(f))
