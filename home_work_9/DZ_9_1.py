# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список


list_number = []
for i in range(0, 5):
    list_number.append(int(input(f'Enter number {i + 1} >: ')))
print(f'Your list = {list_number}')
