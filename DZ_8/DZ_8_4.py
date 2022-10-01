# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789' * 2
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

symbol_len = 0
password = ''

while True:
    symbol_len = int(input('Enter the symbols to generate a password >: '))
    if symbol_len < 4:
        print('Error: invalid digit, repeat input', end='\n\n')

    elif 4 <= symbol_len <= 8:
        for i in range(symbol_len):
            password += random.choice(lower_case + upper_case + digits + punctuation)
        print(f'Your {symbol_len} digit password is >: {password}')
