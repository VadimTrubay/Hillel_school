# Задание 6:
# Пользователь вводит строку в котором есть буквы и цифры,
# необходимо из этой строки спарсить целое число.

test_string = input('Enter test string >: ')
new_string = ''
list_number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

for symbol in test_string:
    if symbol in list_number:
        new_string += symbol
print(new_string)
