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


def delete_item(obj: list, position: int):
    for i in range(len(data)-1, -1, -1):
        for value in data[i].values():
            if value == position:
                del data[i]
    return obj


print(delete_item(data, 2))