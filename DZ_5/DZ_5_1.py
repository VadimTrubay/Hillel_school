# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

num_a = int(input('Enter a >: '))
num_b = int(input('Enter b >: '))
num_c = int(input('Enter c >: '))

if (num_a and num_b and num_c) > 10 and (num_a and num_b // 3):
    print('yes')
else:
    print('no')
