# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

A = []
B = int(input('Enter number N >: '))
for i in range(0, B):
    A.append(int(input(f'Enter number {i + 1} >: ')))

A.reverse()
print(f'revers A = {A}')
