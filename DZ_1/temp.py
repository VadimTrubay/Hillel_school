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

