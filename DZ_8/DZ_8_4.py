# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789' * 2
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

symbol_len = int(input('Еnter the symbols to generate a password >: '))
password = ''

if 4 < symbol_len <= 8:
    for i in range(symbol_len):
        password += random.choice(lower_case + upper_case + digits)
    print(f'Your password is: {password}')

elif symbol_len > 8:
    for i in range(symbol_len):
        password += random.choice(lower_case + upper_case + digits + punctuation)
    print(f'Your password is: {password}')
