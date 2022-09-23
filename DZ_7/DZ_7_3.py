# Программа с помощью библиотеки random генерирует случайное число
# от 1 до 10, задача пользователя угадать это число за 3 попытки.
# В случае если пользователь указал больше загаданного числа,
# то нужно вывести "Бери меньше" и наоборот.

import random

print('Игра угадай число за три попытки.')
hidden_number = random.randint(1, 10)
question = input('Сыграем? yes/no >: ')

if question == 'yes':
    for n in range(1, 4):
        entered_number = int(input(f'Попытка #{n}>: '))
        n += 1
        if entered_number > hidden_number:
            print('Бери меньше')
        elif entered_number < hidden_number:
            print('Бери больше')
        elif entered_number == hidden_number:
            print('Ты угадал, ты красавчик!')
            break
    print('Игра окончена!')
elif question == 'no':
    print('Значит, сыграем в другой раз')
