# Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за
# расположение элемента в списке.
# Position всегда должен быть последовательным, например у нас есть список
# data = [
# {'name': 'Test 1', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 3', 'position': 3},
# ]
# И мы хотим удалить элемент у которого position = 2,
# то на выходе мы должны получить следующий список:
# data = [
# {'name': 'Test 1', 'position': 1},
# {'name': 'Test 3', 'position': 2},  # -1
# ]
# Придерживаясь такой логики, необходимо реализовать:
# 1. Удаление элемента
# 2. Добавление элемента с любым position, например мы хотим в наш исходный список добавить элемент
# у которого position = 1, то должны получить:
# data = [
# {'name': 'Test 4', 'position': 1}
# {'name': 'Test 1', 'position': 2},  # +1
# {'name': 'Test 2', 'position': 3},  # +1
# {'name': 'Test 3', 'position': 4},  # +1
# ]
# 3. Поменять элементы местами, например position 1 и position 3,
# то должны получить следующий список:
# data = [
# {'name': 'Test 3', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 1', 'position': 3},
# ]
# Функционал необходимо реализовать с помощью функций!

data = [
    {
        'name': 'Test 1',
        'position': 1
    },
    {
        'name': 'Test 2',
        'position': 2
    },
    {
        'name': 'Test 3',
        'position': 3
    },
]

for i in range(len(data)):
    # print(data[i])
    for key in range(data[i].keys()):
        print(key)


# def vad(key, value):
#     if key in data:
#         return data
#
#
# print(vad('name', 'position'))


