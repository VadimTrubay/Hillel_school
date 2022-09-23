# Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.

for num_1 in list(range(1, 11)):
    for num_2 in list(range(1, 11)):
        result = num_2 * num_1
        print(f'{num_1}*{num_2}={result}')
