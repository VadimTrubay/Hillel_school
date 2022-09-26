# Задание 5:
# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
# что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

test_string = input('Enter test string >: ')

if test_string.find('@') != -1 and \
        test_string.find('.') != -1:
    print('YES')
else:
    print('NO')
