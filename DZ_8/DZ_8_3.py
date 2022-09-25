# Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и
# выводит свой результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя все буквы в нижнем регистре
# 3 - у пользователя есть буквы в нижнем регистре и цифры
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

password = input('Enter password to verify >: ')
space = 0
lower = 0
upper = 0
digit = 0
lenght = 0

if password == 'qwerty' or password == 'admin' or password == '':  # 1 сложность
    print('Password complexity is 1')
    exit()

for symbol in password:  # 5 сложность
    if symbol.isspace():
        space += 1
    if symbol.islower():
        lower += 1
    if symbol.isupper():
        upper += 1
    if symbol.isdigit():
        digit += 1
    if len(password):
        lenght += 1
if upper != 0 and lower != 0 \
        and digit != 0 and space != 0 \
        and lenght > 8:
    print('Password complexity is 5')
    exit()

for symbol in password:  # 4 сложность
    if symbol.islower():
        lower += 1
    if symbol.isdigit():
        digit += 1
    if symbol.isupper():
        digit += 1
if lower != 0 and digit != 0 and upper != 0:
    print('Password complexity is 4')
    exit()

for symbol in password:  # 3 сложность
    if symbol.islower():
        lower += 1
    if symbol.isdigit():
        digit += 1
if lower != 0 and digit != 0:
    print('Password complexity is 3')
    exit()

if password.islower():  # 2 сложность
    print('Password complexity is 2')
    exit()
