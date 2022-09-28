# Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и
# выводит свой результат в оценочной шкале от 1 до 5.
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
# 3 - у пользователя есть буквы в нижнем регистре и цифры
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

enter_password = input('Enter password to verify >: ')
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
symbol_punctuation = 0
symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

if enter_password == 'qwerty' or enter_password == 'admin' or enter_password == '':  # 1 сложность
    print('Password complexity is 1')
    exit()

for symbol in enter_password:  # 5 сложность
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    if symbol.isupper():
        symbol_upper += 1
    if symbol.isdigit():
        symbol_digit += 1
all_symbols = symbol_punctuation + symbol_lower + symbol_upper + symbol_digit
if symbol_upper != 0 and symbol_lower != 0 \
        and symbol_digit != 0 and symbol_punctuation != 0 \
        != 0 and all_symbols >= 8:
    print(all_symbols)
    print('Password complexity is 5')
    print(all_symbols)
    print(symbol_punctuation)
    print(symbol_digit)
    print(symbol_upper)
    print(symbol_lower)
    exit()

# for symbol in enter_password:  # 4 сложность
#     for i in punctuation:
#         if i == symbol:
#             symbol_punctuation += 1
#     if symbol.islower():
#         symbol_lower += 1
#     if symbol.isdigit():
#         symbol_digit += 1
#     if symbol.isupper():
#         symbol_upper += 1
# all_symbols = symbol_punctuation + symbol_space + symbol_lower + symbol_upper + symbol_digit
# if symbol_lower != 0 and symbol_digit != 0 \
#         and symbol_upper != 0 and all_symbols < 8:
#     print(all_symbols)
#     print('Password complexity is 4')
#     exit()
#
# for symbol in enter_password:  # 3 сложность
#     if symbol.islower():
#         symbol_lower += 1
#     if symbol.isdigit():
#         symbol_digit += 1
#     if symbol.isupper():
#         symbol_upper += 1
# if symbol_lower != 0 and symbol_digit != 0 or \
#         symbol_lower != 0 and symbol_upper != 0 or \
#         symbol_digit != 0 and symbol_upper != 0:
#     print('Password complexity is 3')
#     exit()
#
# for symbol in enter_password:  # 2 сложность
#     for i in punctuation:
#         if i == symbol:
#             symbol_punctuation += 1
# if enter_password.islower() or \
#         enter_password.isupper() or \
#         enter_password.isdigit() or \
#         symbol_punctuation != 0:
#     print('Password complexity is 2')
#     exit()
