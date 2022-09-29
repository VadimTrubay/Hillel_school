# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

input_number = 1
A = []
C = []

for i in range(0, 5):
    A.append(int(input(f'Enter number {input_number} >: ')))
    input_number += 1
for j in A:
    if j > 5:
        C.append(j)
print(f'C (number > 5) = {C}')
