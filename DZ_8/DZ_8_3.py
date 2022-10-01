# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
# 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
# 3- у пользователя в пароле соблюдается два условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
# у пользователя в пароле соблюдается три условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

enter_password = input('Enter password to verify >: ')
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
symbol_punctuation = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

if enter_password == 'qwerty' or \
        enter_password == 'admin' or \
        enter_password == '':  # 1 сложность
    print('Password complexity is 1')
    exit()

for symbol in enter_password:  # 5 сложность
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isupper():
        symbol_upper += 1
    elif symbol.isdigit():
        symbol_digit += 1
all_symbols = symbol_punctuation + symbol_lower + symbol_upper + symbol_digit
if symbol_upper != 0 and symbol_lower != 0 \
        and symbol_digit != 0 and symbol_punctuation != 0 \
        and all_symbols >= 8:
    print('Password complexity is 5')
    exit()

for symbol in enter_password:  # 4 сложность
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isdigit():
        symbol_digit += 1
    elif symbol.isupper():
        symbol_upper += 1
if symbol_lower != 0 and symbol_digit != 0 \
        and symbol_upper != 0:
    print('Password complexity is 4')
    exit()

for symbol in enter_password:  # 3 сложность
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
    if symbol.islower():
        symbol_lower += 1
    elif symbol.isdigit():
        symbol_digit += 1
    elif symbol.isupper():
        symbol_upper += 1
if symbol_lower != 0 and symbol_digit != 0 or \
        symbol_lower != 0 and symbol_upper != 0 or \
        symbol_lower != 0 and symbol_punctuation != 0 or \
        symbol_digit != 0 and symbol_upper != 0 or \
        symbol_digit != 0 and symbol_punctuation != 0 or \
        symbol_upper != 0 and symbol_punctuation != 0:
    print('Password complexity is 3')
    exit()

for symbol in enter_password:  # 2 сложность
    for i in punctuation:
        if i == symbol:
            symbol_punctuation += 1
if enter_password.islower() or \
        enter_password.isupper() or \
        enter_password.isdigit() or \
        symbol_punctuation != 0:
    print('Password complexity is 2')
    exit()
