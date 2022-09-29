# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла
# (запрещено использовать функцию min и max).
# Вывести эти числа.

input_number = 1
A = []
B = int(input(f'Enter number N >: '))

for i in range(0, B):
    A.append(int(input(f'Enter number {input_number} >: ')))
    input_number += 1

min_value = A[0]
max_value = 0

for j in A:
    if j > max_value:
        max_value = j
    elif j < min_value:
        min_value = j
print(f'min_value = {min_value}, max_value = {max_value}')
