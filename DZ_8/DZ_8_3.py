# Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и
# выводит свой результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя все буквы в нижнем регистре
# 3 - у пользователя есть буквы в нижнем регистре и цифры
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

enter_password = input('Enter password to verify >: ')
symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0
len_password = 0

if enter_password == 'qwerty' or enter_password == 'admin' or enter_password == '':  # 1 сложность
    print('Password complexity is 1')
    exit()

for symbol in enter_password:  # 5 сложность
    if symbol.isspace():
        symbol_space += 1
    if symbol.islower():
        symbol_lower += 1
    if symbol.isupper():
        symbol_upper += 1
    if symbol.isdigit():
        symbol_digit += 1
    if len(enter_password):
        len_password += 1
if symbol_upper != 0 and symbol_lower != 0 \
        and symbol_digit != 0 and symbol_space != 0 \
        and len_password > 8:
    print('Password complexity is 5')
    exit()

for symbol in enter_password:  # 4 сложность
    if symbol.islower():
        symbol_lower += 1
    if symbol.isdigit():
        symbol_digit += 1
    if symbol.isupper():
        symbol_upper += 1
if symbol_lower != 0 and symbol_digit != 0 and symbol_upper != 0:
    print('Password complexity is 4')
    exit()

for symbol in enter_password:  # 3 сложность
    if symbol.islower():
        symbol_lower += 1
    if symbol.isdigit():
        symbol_digit += 1
if symbol_lower != 0 and symbol_digit != 0:
    print('Password complexity is 3')
    exit()

if enter_password.islower():  # 2 сложность
    print('Password complexity is 2')
    exit()
