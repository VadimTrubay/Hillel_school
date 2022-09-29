# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

input_number = 1
A = []
B = int(input(f'Enter number N >: '))
for i in range(0, B):
    A.append(int(input(f'Enter number {input_number} >: ')))
    input_number += 1
A.reverse()
print(A)


