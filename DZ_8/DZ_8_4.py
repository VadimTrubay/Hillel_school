# Напишите программу где пользователь вводит число symbol_len,
# а программа генерирует пароль длинной symbol_len.
# Чем выше будет сложность пароля, тем лучше.
# Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

all_symbols = lower_case + upper_case + digits + punctuation

symbol_len = int(input('Еnter the symbols to generate a password >: '))
password = ''

for i in range(symbol_len):
    password += random.choice(all_symbols)
print(f'Your password is: {password}')
