# Задание 5:
# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
# что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

string = input('Enter test string >: ')

if '@' in string:
    print('YES')
elif '.' in string:
    print('YES')
else:
    print('NO')
