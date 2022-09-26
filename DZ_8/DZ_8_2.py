# Напишите программу где пользователь вводит число - count,
# а программа выводит count чисел фибоначчи.

number = int(input('Enter number >: '))
fib_num_1 = 0
fib_num_2 = 1

if number == 0:
    print(0)
    exit(4)
else:
    print(fib_num_1)
for i in range(number + 1):
    fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2
    print(fib_num_1)
