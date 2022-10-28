# Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за
# расположение элемента в списке.
# Position всегда должен быть последовательным, например у нас есть список
# 2. Добавление элемента с любым position, например мы хотим в наш исходный список добавить элемент
# у которого position = 1, то должны получить:
# data = [
# {'name': 'Test 4', 'position': 1}
# {'name': 'Test 1', 'position': 2},  # +1
# {'name': 'Test 2', 'position': 3},  # +1
# {'name': 'Test 3', 'position': 4},  # +1
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


def add_pos(lst, pos_num, pos):
    new_dict = {'name': f'{pos} {len(lst) + 1}', 'position': None}
    lst.insert(pos_num - 1, new_dict)

    for i, value in enumerate(lst):
        value['position'] = (i + 1)
    return lst
