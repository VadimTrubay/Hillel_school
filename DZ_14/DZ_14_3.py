# 3. Поменять элементы местами, например position 1 и position 3,
# то должны получить следующий список:
# data = [
# {'name': 'Test 3', 'position': 1},
# {'name': 'Test 2', 'position': 2},
# {'name': 'Test 1', 'position': 3},
# ]
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
    }
]


def change_pos(lst, pos_1, pos_2):
    lst.insert(pos_1 - 1, lst[pos_2 - 1])
    lst.pop(pos_2)
    lst.insert(pos_2, lst[pos_1])
    lst.pop(pos_1)

    for key, value in enumerate(lst):
        value['position'] = (key + 1)
    return lst


pprint.pprint(change_pos(data, 1, 3))
