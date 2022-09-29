# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество цифр: 3

amount_digit = 0
text = input('Enter text >: ')
text.split(' ')
for i in text:
    if i.isdigit():
        amount_digit += 1

print(amount_digit)
