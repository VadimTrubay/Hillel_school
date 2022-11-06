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
# Функционал необходимо реализовать с помощью функций!
import pprint

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
    {
        'name': 'Test 4',
        'position': 4
    },
    {
        'name': 'Test 5',
        'position': 5
    }
]


def del_pos(lst, pos_num):
    lst.pop(pos_num - 1)
    for key, value in enumerate(lst):
        value['position'] = (key + 1)
    return lst


pprint.pprint(del_pos(data, 3))
