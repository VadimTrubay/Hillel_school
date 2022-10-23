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


def delete_item(obj: list, position: int):
    for i in range(len(data)):
        for value in data[i].values():
            if value == position:
                data.append(data[i])
    return obj


print(delete_item(data, 4))
