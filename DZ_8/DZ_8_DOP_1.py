# Задание 1:
# Пользователь вводит слово, если это слово является
# полиндромом, то вывести '+', иначе '-'

enter_text = input('Enter text >: ')

if enter_text == enter_text[::-1]:
    print('+')
else:
    print('-')
