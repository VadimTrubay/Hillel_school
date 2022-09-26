# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

symbol_len = int(input('Еnter the symbols to generate a password\n'
                       '(only 4, 6 or 10 symbols) >: '))

if 0 <= symbol_len < 4 or symbol_len == 5 \
        or 6 < symbol_len <= 9 or symbol_len > 10:
    print('Error: Invalid symbol')
    exit(4)

if symbol_len == 4:
    symbols_1 = random.choices(lower_case, k=2)
    symbols_2 = random.choices(digits, k=2)
    password = symbols_1 + symbols_2
    random.shuffle(password)
    password = ''.join(password)
    print(f'Your password is: {password}')

elif symbol_len == 6:
    symbols_1 = random.choices(lower_case, k=2)
    symbols_2 = random.choices(digits, k=2)
    symbols_3 = random.choices(upper_case, k=2)
    password = symbols_1 + symbols_2 + symbols_3
    random.shuffle(password)
    password = ''.join(password)
    print(f'Your password is: {password}')

elif symbol_len == 10:
    symbols_1 = random.choices(lower_case, k=3)
    symbols_2 = random.choices(digits, k=3)
    symbols_3 = random.choices(upper_case, k=2)
    symbols_4 = random.choices(punctuation, k=2)
    password = symbols_1 + symbols_2 + symbols_3 + symbols_4
    random.shuffle(password)
    password = ''.join(password)
    print(f'Your password is: {password}')
