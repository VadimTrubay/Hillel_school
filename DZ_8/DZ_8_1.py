"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
1. isspace
2. islower
3. isupper
4. isdigit
"""

string = input('Введите тестовую строку>: ')
space = 0
lower = 0
upper = 0
digit = 0

for symbol in string:
    if symbol.isspace():
        space += 1
    if symbol.islower():
        lower += 1
    if symbol.isupper():
        upper += 1
    if symbol.isdigit():
        digit += 1

if upper != 0 and lower != 0 and digit != 0 and space != 0:
    print('YES')
else:
    print('NO')
