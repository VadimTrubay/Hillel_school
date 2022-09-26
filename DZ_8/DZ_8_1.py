"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
1. isspace
2. islower
3. isupper
4. isdigit
"""

test_string = input('Enter test string >: ')
symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

for symbol in test_string:
    if symbol.isspace():
        symbol_space += 1
    if symbol.islower():
        symbol_lower += 1
    if symbol.isupper():
        symbol_upper += 1
    if symbol.isdigit():
        symbol_digit += 1
all_symbols = symbol_lower and symbol_upper and symbol_digit and symbol_space
if all_symbols != 0:
    print('YES')
else:
    print('NO')
