# 2 Дан многомерный список. Вывести на экран все нечетные столбцы,
# у которых первый элемент больше последнего.
# исходный список
# [1 6 8 5 4 0 3]
# [5 7 8 9 4 2 1],
# [6 0 7 8 1 2 5],
# [5 7 2 7 5 2 1]

# результат работы кода с задания 2
# 8 3
# 8 1
# 7 5
# 2 1

a = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
    ]

for x, x_value in enumerate(a):
    # print(x, x_value)
    for y, y_value in enumerate(x_value):
        if y % 2 == 0:
            print(x, y_value)


