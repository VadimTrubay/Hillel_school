# Пользователь вводит текст, удалить в
# тексте все цифры и вывести строку пользователю.

test_string = input('Enter test string >: ')
new_string = ''
list_number = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

for symbol in test_string:
    if symbol not in list_number:
        new_string += symbol
print(new_string)
