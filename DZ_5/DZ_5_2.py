# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

num_a = int(input('Enter a >: '))
num_b = int(input('Enter b >: '))
num_c = int(input('Enter c >: '))
max = 0
if num_a >= num_b and num_a >= num_c:
    max = num_a
if num_b >= num_a and num_b >= num_c:
    max = num_b
if num_c >= num_a and num_c >= num_b:
    max = num_c
print(f'Наибольшее число равно: {max}')
