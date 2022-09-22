# Программа с помощью библиотеки random генерирует случайное число
# от 1 до 10, задача пользователя угадать это число за 3 попытки.
# В случае если пользователь указал больше загаданного числа,
# то нужно вывести "Бери меньше" и наоборот.

import random
import time

print('Игра угадай число за три попытки.')
time.sleep(1)
hidden_number = random.randint(1, 10)
print(hidden_number)
while True:
    question = input('Сыграем? y/n >: \n')
    time.sleep(1)
    if question == 'y':

        entered_number = int(input('Попытка #1 <ввод тут>: '))
        if entered_number > hidden_number:
            print('Бери меньше')
        elif entered_number < hidden_number:
            print('Бери больше')
        else:
            print('Ты угадал, ты красавчик!')
            break
        time.sleep(1)

        entered_number = int(input('Попытка #2 <ввод тут>: '))
        if entered_number > hidden_number:
            print('Бери меньше')
        elif entered_number < hidden_number:
            print('Бери больше')
        else:
            print('Ты угадал, ты красавчик!')
            break
        time.sleep(1)

        entered_number = int(input('Попытка #3 <ввод тут>: '))
        if entered_number == hidden_number:
            print('Ты угадал, ты красавчик!')
            break
        else:
            print('Ты не угадал! Не отчаивайся, повезёт в следующий раз!')
            break

    elif question == 'n':
        print('Значит сыграем в другой раз')
        break
    time.sleep(1)
time.sleep(1)
print('До новых встреч!')
