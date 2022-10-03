# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N


A = []
for i in range(0, 10):
    A.append(int(input(f'Enter number {i + 1} >: ')))
B = int(input('Enter number N >: '))
amount_N = 0
for j in A:
    if j == B:
        amount_N += 1

print(f'In the list A the number N is repeated {amount_N} times')
