# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество цифр: 3

amount_digits = 0
new_string = ''
text = input('Enter text >: ')
text = text.split(' ')

for i in text:
    if i.isdigit():
        amount_digits += 1

print(f'amount_digits = {amount_digits}')
