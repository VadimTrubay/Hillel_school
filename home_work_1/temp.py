# # # Задание 1
# # # Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в
# # # списке. Position всегда должен быть последовательным, например у нас есть список
# # # Придерживаясь такой логики, необходимо реализовать:
# # # Удаление элемента
# #
# # from pprint import pprint
# #
# # data = [
# #     {'name': 'Test 1', 'position': 1},
# #     {'name': 'Test 2', 'position': 2},
# #     {'name': 'Test 3', 'position': 3},
# #     {'name': 'Test 4', 'position': 4},
# #     {'name': 'Test 5', 'position': 5}
# # ]
# #
# #
# # def delete_pos(lst, position_number):
# #     lst.pop(position_number - 1)
# #     for i, i_value in enumerate(lst):
# #         i_value['position'] = (i + 1)
# #     return lst
# #
# #
# # pprint(delete_pos(data, 2))
# #
# # # Задача 2
# # # Добавление элемента с любым position, например мы хотим в наш исходный список добавить
# # # элемент у которого position = 1, то должны получить:
# #
# # from pprint import pprint
# #
# # data = [
# #     {'name': 'Test 1', 'position': 1},
# #     {'name': 'Test 2', 'position': 2},
# #     {'name': 'Test 3', 'position': 3},
# # ]
# #
# #
# # def add_pos(lst, position_number, arg_for_pos):
# #     new_dict = {'name': f'{arg_for_pos} {len(lst) + 1}', 'position': None}
# #     lst.insert(position_number - 1, new_dict)
# #
# #     for i, i_value in enumerate(lst):
# #         i_value['position'] = (i + 1)
# #     return lst
# #
# #
# # pprint(add_pos(data, 1, 'Test'))
# #
# # # Задание 3
# # # Поменять элементы местами, например position 1 и position 3, то должны получить следующий список:
# #
# # from pprint import pprint
# #
# # data = [
# #     {'name': 'Test 1', 'position': 1},
# #     {'name': 'Test 2', 'position': 2},
# #     {'name': 'Test 3', 'position': 3},
# #
# # ]
# #
# #
# # def change_pos(lst, pos_for_change_1, pos_for_change_2):
# #     lst.insert(pos_for_change_1 - 1, lst[pos_for_change_2 - 1])
# #     lst.pop(pos_for_change_2)
# #     lst.insert(pos_for_change_2, lst[pos_for_change_1])
# #     lst.pop(pos_for_change_1)
# #
# #     for i, i_value in enumerate(lst):
# #         i_value['position'] = (i + 1)
# #
# #     return lst
# #
# #
# # pprint(change_pos(data, 1, 3))
# #
# #
# # # Задание 1
# # # Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# # # В исходном списке минимум 2 элемента.
# #
# #
# # def change(lst: list) -> list:
# #     lst[0], lst[-1] = lst[-1], lst[0]
# #     return lst
# #
# #
# # a = [4, 8, 2, 'qwert', '@#$']
# # print(change(a))
#
#
# # Задание 1
# # Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# # в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут
# # соответствовать правилам задания ключей в словарях.
#
#
# # def to_dict(lst):
# #     a = dict(zip(lst, lst))
# #     return a
#
# #
# # lst = [4, 15, 254, 'qwer', '123@@']
# # print(to_dict(lst))
#
#
# # Задание 3
# # Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
# # до величины «end» включительно.Если пользователь задаст первое число большее чем второе,
# # просто поменяйте их местами.
#
# # def sum_range(start: int, end: int):
# #     a = 0
# #     if start > end:
# #         start, end = end, start
# #     for i in range(start, end + 1):
# #         a += i
# #     return a
# #
# #
# # print(sum_range(4, 9))
#
#
# # Задание 4
# # Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# # и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# # что задано положительное целое число).
#
#
# # def read_last(lines, file):
# #     if lines > 0:
# #         a = open(file, 'r')
# #         strings = a.readlines()[-lines:]
# #         for i in strings:
# #             print(i)
# #         a.close()
# #
# #     else:
# #         print("Неверно, должно быть задано положительное целое число ")
# #
# #
# # read_last(5, 'for 13.txt')
#
# # Задание №1
# # Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# # В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк
#
# #
# # import pickle
# #
# # job_title = [
# #     {
# #         'name': 'Alexandr',
# #         'position': 'engineer',
# #     },
# #     {
# #         'name': 'Maksim',
# #         'positione': 'director'
# #     }
# # ]
# #
# # file = open('omtp.com.ua', 'wb')
# # file.write(pickle.dumps(job_title))
# # file.close()
# # # Задание 2
# # Дано два словаря
# # Необходимо написать код который будет их объединять
# # Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы
# # не потерять значения нужно записать в один ключ список в котором будут находится значения
# # Записать результат в файл result.json в формате JSON.
#
# # import json
# #
# # fast_car = {
# #     'drift': 'nissan',
# #     'price': '32k'
# # }
# # comfort_car = {
# #     'drift': 'mazda',
# #     'starting price': '42000$'
# # }
# # same_keys = {}
# # for key, value in fast_car.items():
# #     for key1, value1 in comfort_car.items():
# #         if key == key1:
# #             same_keys[key1] = [value, value1]
# #         else:
# #             break
# #
# # diff_keys = fast_car | comfort_car
# # result = diff_keys | same_keys
# #
# # json_result = json.dumps(result)
# # with open('result.json', 'w') as file:
# #     file.write(json_result)
#
# # Задание #1
# # Дано два множества A и B
# # В множестве А находятся имена должников за Сентябрь
# # В множестве B находятся имена должников за Октябрь
# # Найти:
# # * Вывести имена людей которые должны за Сентябрь и Октябрь
# # * Вывести должников за Октябрь у которых нет долга за Сентябрь
# #
# # A = {'Вася ', 'Петя', 'Галя', 'Герасим', 'Коля'}
# # B = {'Артур', 'Коля', 'Герасим', 'Петя', 'Жанна'}
# #
# # print(A | B)
# # print(B - A)
#
# # Задание #2:
# '''Права доступа
# Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
# запись – W;
# чтение – R;
# запуск – X.
# На вход программе подается:
# число n – количество файлов;
# n строк с именами файлов и допустимыми операциями;
# число m – количество запросов к файлам;
# m запросов вида «операция файл».
# Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
# Пример ввода:
# 3
# python.exe X
# book.txt R W
# notebook.exe R W X
# 5
# read python.exe
# read book.txt
# write notebook.exe
# execute notebook.exe
# write book.txt
# Пример вывода:
# Access denied
# OK
# OK
# OK
# OK
# '''
# #
# # n = int(input('количество запросов к файлам: '))
# # keys = {'write': 'W', 'read': 'R', 'execute': 'X'}
# # A = {}
# #
# # for i in range(n):
# #     a, b = input('введите имя файла и права доступа к файлу: ').split()
# #     A[a] = b
# #
# # m = int(input('количество запросов к файлам: '))
# #
# # for i in range(m):
# #     c, d = input('введите разрешение для файла и имя файла: ').split()
# #     if keys[c] in A[d]:
# #         print('ok')
# #     else:
# #         print('Access denied')
#
# #  1 Дан многомерный список. Вывести на экран первый и последний столбцы.
#
#
# A = [
#     [1, 6, 8, 5, 4, 0, 3],
#
#     [5, 7, 8, 9, 4, 2, 1],
#
#     [6, 0, 7, 8, 1, 2, 5],
#
#     [5, 7, 2, 7, 5, 2, 1]
# ]
#
# for i in range(len(A)):
#     F, *centr, L = A[i]
#
#     print(F, L)
#
# # 2 Дан многомерный список. Вывести на экран все четные столбцы, у которых первый элемент больше последнего.
#
#
# A = [[1, 6, 8, 5, 4, 0, 3],
#
#      [5, 7, 8, 9, 4, 2, 1],
#
#      [6, 0, 7, 8, 1, 2, 5],
#
#      [5, 7, 2, 7, 5, 2, 1]]
#
# for i, a in enumerate(A):
#     print(*[A[i][j] for j, b in enumerate(a) if j % 2 == 0 and A[0][j] > A[len(A) - 1][j]])
#
# # Задача 3
# # Дан многомерный список в котором находится результат игры в крестики нолики,
# # выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# # Необходимо учитывать то,что есть разные выигрышные варианты и программа должна их распознавать.
#
#
# Doska = [
#     ['o', 'o', 'x'],
#     ['x', 'o', 'o'],
#     ['x', 'x', 'o']
# ]
#
# n = 0
#
# for i, i_value in enumerate(Doska):
#     V = 0  # hod vas
#     P = 0  # hod pet
#
#     for j, j_value in enumerate(i_value):
#         if str(Doska[i][j]) == 'x':
#             V += 1
#         elif str(Doska[i][j]) == 'o':  #
#             V -= 1
#         if str(Doska[j][i]) == 'x':
#             P += 1
#         elif str(Doska[j][i]) == 'o':
#             P -= 1
#
#         if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'x' or str(Doska[0][2]) == str(
#                 Doska[2][0]) == str(Doska[1][1]) == 'x':
#             n += 1
#         if str(Doska[0][0]) == str(Doska[1][1]) == str(Doska[2][2]) == 'o' or str(Doska[0][2]) == str(
#                 Doska[2][0]) == str(Doska[1][1]) == 'o':
#             n -= 1
#
#         if V == 3 or P == 3 or n == 3:  #
#             print("x win")
#             exit()
#
#         elif V == -3 or P == -3 or n == -3:  #
#             print("o win")
#             exit()
#
#
# else:
#
#     print("Ничья")
#
# def transpose_list(list_of_lists):
#     return [
#         list(row)
#         for row in zip(*list_of_lists)
#     ]
#
#
# print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
# # Задание 1:
# # Запросить у пользователя 5 чисел и записать их в список
#
#
# list_num = []
#
# for num in range(5):
#     i = int(input('Введите число: '))
#     list_num.append(i)
#
# print(list_num)
#
# # Задание 2:
# # Дан список A = [1, 2, 3, 4, 5] Удалить последнее число из списка
#
#
# A = [1, 2, 3, 4, 5]
# del A[-1]
#
# print(A)
#
# # Задание 3:
# # Запросить у пользователя 10 чисел и записать их в список A
# # Запросить у пользователя число N
# # Вывести пользователю сколько в списке A повторяется число N
#
#
# my_list = []
# rep = 0
#
# for num in range(10):
#     x = int(input(f'Введите число {num + 1}: '))
#     my_list.append(x)
#
# N = int(input('Число которое повторяется: '))
#
# for num_2 in my_list:
#     if num_2 == x:
#         rep += 1
#
# print(rep)
#
# # Задание 4:
# # Запросить у пользователя число N
# # Запросить у пользователя N чисел и записать их в список A
# # Вывести список в обратной последовательности
#
#
# N = int(input('Число пользователя N:'))
# number = []
#
# for num in range(N):
#     x = int(input('Введите число: '))
#     number.append(x)
#     number_rev = list(reversed(number))
#
# print('Cписок A =', number)
#
# print('Обратный список =', number_rev)
#
# # Задание 5:
# # Запросить у пользователя 5 чисел и записать их в список A
# # Записать все числа из списка A которые больше 5 в список C
#
# # NO
#
#
# A = []
#
# for num in range(5):
#     x = int(input(f'Введите число {num + 1}: '))
#     A.append(x)
# print('Список А ', A)
# C = []
# for num_2 in A:
#     if num_2 > 5:
#         C.append(num_2)
#
# print('Список C ', C)
#
# # адание 6:
# # Запросить у пользователя число N
# # Запросить у пользователя N целых чисел и записать их в список A
# # Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max).
# # Вывести эти числа.
#
#
# A = []
# N = int(input('Число пользователя N:'))
#
# for num in range(N):
#     x = int(input('Введите число: '))
#     A.append(x)
# sorted(A)
#
# print('Список А =', A)
# a, *_, b = A
#
# print(f'Min =', a)
# print(f'Max =', b)
#
# # Задание 7:
# # Пользователь вводит текст нужно вывести количество цифр в этом тексте
#
#
# a = input('Введите строку; ')
#
# num = [int(i) for i in a if i.isdigit()]
# print('Количество цифр в тексте:', len(num))
#
# #  Задание 1  Написать программу которая проверяет что в строке есть хотя бы один пробел,
# # число, буква нижнего и верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'
#
#
# import string
#
# test_string = input('Введите строку: ')
#
# symbol_space = 0
# symbol_lower = 0
# symbol_upper = 0
# symbol_digit = 0
#
# for symbol in test_string:
#     if symbol.isspace():
#         symbol_space += 1
#     elif symbol.islower():
#         symbol_lower += 1
#     elif symbol.isupper():
#         symbol_upper += 1
#     elif symbol.isdigit():
#         symbol_digit += 1
# if symbol_lower != 0 and symbol_upper != 0 and symbol_digit != 0 and symbol_space != 0:
#     print('YES')
# else:
#     print('NO')
#
# # Задание 2 Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.
#
#
# count = int(input('Веди число: '))
#
# f1 = f2 = 1
# print(f1, f2, end=' ')
# i = 2
# while i < count:
#     f1, f2 = f2, f1 + f2
#     print(f2, end=' ')
#     i += 1
# print()
#
# # Задаине №3 Напишите программу где пользователь вводит пароль, а программа проверяет сложность
# # пароля и выводит свой результат в оценочной шкале от 1 до 5.
#
#
# lower_case = 0
# upper_case = 0
# special = 0
# digits = 0
# password = input('Введите пароль на проверку: ')
#
# if password == 'qwerty' or password == 'admin' or password == '':
#     print('Оценка сложности пароля -', 1)
#     exit()
#
# for i in range(len(password)):
#     if str(password[i]).islower():
#         lower_case += 1
#     elif str(password[i]).isupper():
#         upper_case += 1
#     elif str(password[i]).isnumeric():
#         digits += 1
#     else:
#         special += 1
#
# if lower_case == len(password) or upper_case == len(password) or digits == len(password) or special == len(
#         password):
#     print('Оценка сложности пароля -', 2)
#
# elif lower_case > 0 and digits > 0 and upper_case == 0 and special == 0:
#     print('Оценка безопастности пароля -', 3)
# elif lower_case > 0 and upper_case > 0 and digits == 0 and special == 0:
#     print('Оценка сложности пароля -', 3)
# elif lower_case > 0 and special > 0 and digits == 0 and upper_case == 0:
#     print('Оценка сложности пароля -', 3)
# elif upper_case > 0 and special > 0 and digits == 0 and lower_case == 0:
#     print('Оценка сложности пароля -', 3)
# elif upper_case > 0 and digits > 0 and special == 0 and lower_case == 0:
#     print('Оценка сложности пароля -', 3)
# elif special > 0 and digits > 0 and upper_case == 0 and lower_case == 0:
#     print('Оценка сложности пароля -', 3)
#
# elif lower_case > 0 and digits > 0 and upper_case > 0 and special == 0:
#     print('Оценка сложности пароля -', 4)
# elif special > 0 and digits > 0 and upper_case > 0 and lower_case == 0:
#     print('Оценка сложности пароля -', 4)
# elif lower_case > 0 and digits > 0 and special > 0 and upper_case == 0:
#     print('Оценка сложности пароля -', 4)
# elif lower_case > 0 and special > 0 and upper_case > 0 and digits == 0:
#     print('Оценка сложности пароля -', 4)
#
# elif lower_case > 0 and digits > 0 and upper_case > 0 and special > 0 and len(password) > 8:
#     print('Оценка сложности пароля -', 5)
#
# # Задание №4 Напишите программу где пользователь вводит число symbol_len, а программа генерирует
# # пароль длинной symbol_len. Чем выше будет сложность пароля, тем лучше. Сложность пароля буду
# # оценивать по шкале от 1 до 5 из задании #3
# #
#
#
# import random
# import string
#
# symbol_len = int(input('Длина пароля:'))
#
# lower_case = 'abcdefghijklmnopqrstuvwxyz'
# upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# special = '()[]{}@# %^&*_+-='
# digits = '0123456789'
#
# all = lower_case + upper_case + special + digits
# passworld = ''.join(random.sample(all, symbol_len))
#
# upper_case = any([1 if i in string.ascii_uppercase else 0 for i in passworld])
# lower_case = any([1 if i in string.ascii_lowercase else 0 for i in passworld])
# special = any([1 if i in string.punctuation else 0 for i in passworld])
# digits = any([1 if i in string.digits else 0 for i in passworld])
# length = symbol_len
#
# if length >= 8:
#     length = True
# else:
#     length = False
#
# characters = [upper_case, lower_case, special, digits, length]
#
# score = 0
#
# for i in range(len(characters)):
#     if characters[i]:
#         score += 1
#
# print('Надежность пароля: %s из 5' % score)
#
# print('Ваш пaроль: ' + passworld)
#
# # Задание 1:
# #  Необходимо вывести на экран числа от 5 до 1 с помощью цикла for.
#
# for i in range(5, 0, -1):
#     print(i, end=' ')
#
# # Задание 4:
# # Вывести на экран таблицу умножения от 1 до 10 с помощью двух циклов for.
#
# for i in range(1, 11):
#
#     for n in range(1, 11):
#         print(n, '*', i, '=', n * i, sep='', end='    ')
#     print()
#
# # Задание 2:
# #  Вывести таблицу умножения на 3 с помощью цикла for.
#
#
# for i in range(1, 11):
#     print('3*', i, '=', 3 * i, sep='')
#
# # Задание 3:
# # Программа с помощью библиотеки random генерирует случайное число от 1 до 10,
# # задача пользователя угадать это число за 3 попытки. В случае если пользователь
# # указал больше загаданного числа, то нужно вывести "Бери меньше" и наоборот.
#
#
# import random
#
# n = 0
# for i in range(1, 11):
#
#     print(f'Попытка №', n + 1)
#     a = int(input(':'))
#
#     if a == i:
#         print('Ты угадал!')
#         break
#     if a < i:
#         print('Бери больше')
#     else:
#         print('Бери меньше')
#     n += 1
#     if n == 3:
#         break
#
# # Вывести треугольник #1 с шириной N с помощью цикла while
#
# N = int(input("Please input number :"))
#
# num_height = 1
#
# while num_height <= N:
#     num_width = N
#     while num_width >= num_height:
#         print("*", end='')
#         num_width -= 1
#     num_height += 1
#     print()
#
# # Вывести треугольник #2 с шириной N с помощью цикла while
#
# N = int(input("Please input number :"))
#
# h = 1
#
# while h <= N:
#     w = 1
#     while w <= h:
#         print("*", end="")
#         w += 1
#     h += 1
#     print()
#
# # Вывести треугольник #3 с шириной N с помощью цикла while
#
# N = int(input("Please input number :"))
# i = N
#
# print(('*') * i)
# while i != 1:
#     i -= 1
#
#     print((' ') * (N - i) + (('*') * i))
#
# # Задание 1
# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
#
# if min(a, b, c) > 10 and a % 3 == 0 and b % 3 == 0:
#     print('Yes')
# else:
#     print('No')
#
# # Задание 2
#
# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# c = int(input('Введите число c: '))
#
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
#
# print(f'max: ', max)
#
# # Задания со звездочкой:
#
# number = int(input('Введите 3х значное число:'))
# if not 100 <= number <= 999:
#     print('Ошибка, число не входит в диапазон')
#     exit()
#
# first_num = number % 10
# second_num = number % 100 // 10
# third_num = number % 1000 // 100
# final_num = first_num * 100 + second_num * 10 + third_num
# print(final_num)
# a = [
#     [1, 6, 8, 5, 4, 0, 3],
#     [5, 7, 8, 9, 4, 2, 1],
#     [6, 0, 7, 8, 1, 2, 5],
#     [5, 7, 2, 7, 5, 2, 1]
# ]
# for i in range(len(a)):
#     F, *centr, L = a[i]
#     print(F, L)


# from re import search
# j = 'Oceans'
# key = 'ocean'
# reg = bool(search(f'{j.lower()}\-', key))
# print(reg)

j = 'Oceans'
key = 'Ocean'
if key in j:
    print('Ok')