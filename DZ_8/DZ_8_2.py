# Напишите программу где пользователь вводит число - count,
# а программа выводит count чисел фибоначчи.

count = int(input('Введите число >: '))
fib_num_1 = 0
fib_num_2 = 1

if count == 0:
    print(0)
    exit(4)
else:
    print(0)
for i in range(count + 1):
    fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
    print(fib_num_1)
