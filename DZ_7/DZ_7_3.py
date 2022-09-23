# Программа с помощью библиотеки random генерирует случайное число
# от 1 до 10, задача пользователя угадать это число за 3 попытки.
# В случае если пользователь указал больше загаданного числа,
# то нужно вывести "Бери меньше" и наоборот.

import random

print('Игра угадай число за три попытки.')
hidden_number = random.randint(1, 10)

while True:
    question = input('Сыграем? yes/no >: ')
    if question == 'yes':

        entered_number_1 = int(input('Попытка #1 <ввод тут>: '))
        if entered_number_1 > hidden_number:
            print('Бери меньше')
        elif entered_number_1 < hidden_number:
            print('Бери больше')
        else:
            print('Ты угадал, ты красавчик!')
            break

        entered_number_2 = int(input('Попытка #2 <ввод тут>: '))
        if entered_number_2 > hidden_number:
            print('Бери меньше')
        elif entered_number_2 < hidden_number:
            print('Бери больше')
        else:
            print('Ты угадал, ты красавчик!')
            break

        entered_number_3 = int(input('Попытка #3 <ввод тут>: '))
        if entered_number_3 == hidden_number:
            print('Ты угадал, ты красавчик!')
            break
        else:
            print('Ты не угадал! Не отчаивайся, повезёт в следующий раз!')
            break

    elif question == 'no':
        print('Значит, сыграем в другой раз')
        break
print('До новых встреч!')
