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
print(password)



# symbols_lower_case = random.choices(lower_case, k=1)
# symbols_digits = random.choices(digits, k=1)
# symbols_upper_case = random.choices(upper_case, k=1)
# characters = random.choices(punctuation, k=1)
#
# symbol_len = int(input('Еnter the symbols to generate a password >: '))
#
# if symbol_len == 0:
#     print('Error: Invalid symbol')
#     exit(4)
#
# def generate(symbol_len):


#
# if symbol_len == 4:
#     symbols_1 = random.choices(lower_case, k=2)
#     symbols_2 = random.choices(digits, k=2)
#     password = symbols_1 + symbols_2
#     random.shuffle(password)
#     password = ''.join(password)
#     print(f'Your password is: {password}')

