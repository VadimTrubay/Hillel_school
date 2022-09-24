# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
space = ' '

symbol_len = int(input('Введите количество символов для генерации пароля\n'
                       '(только 4, 6 или 9 символов >: '))

if 0 <= symbol_len < 4 or symbol_len == 5 \
        or 6 < symbol_len <= 8 or symbol_len > 9:
    print('Error: Invalid symbol ')
    exit(4)

if symbol_len == 4:
    symbols_1 = random.choices(lowercase, k=2)
    symbols_2 = random.choices(digits, k=2)
    password = symbols_1 + symbols_2
    random.shuffle(password)
    password = ''.join(password)
    print(f'Вот Ваш пароль: {password}')

elif symbol_len == 6:
    symbols_1 = random.choices(lowercase, k=2)
    symbols_2 = random.choices(digits, k=2)
    symbols_3 = random.choices(uppercase, k=2)
    password = symbols_1 + symbols_2 + symbols_3
    random.shuffle(password)
    password = ''.join(password)
    print(f'Вот Ваш пароль: {password}')

elif symbol_len == 9:
    symbols_1 = random.choices(lowercase, k=3)
    symbols_2 = random.choices(digits, k=3)
    symbols_3 = random.choices(uppercase, k=2)
    symbols_4 = random.choices(space, k=1)
    password = symbols_1 + symbols_2 + symbols_3 + symbols_4
    random.shuffle(password)
    password = ''.join(password)
    print(f'Вот Ваш пароль: {password}')
