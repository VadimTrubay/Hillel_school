# Задание 5:
"""Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре
со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование
с помощью Python.
Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее
зашифровать и вывести на экран.
"""
import sys

text = input('Шифр-машина Цезаря готова к работе\nВведите текст: ').lower()
number = int(input('Введите количество символов сдвига(цифра): '))
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' * 2
alphabet_eng = 'abcdefghijklmnopqrstuvwxyz' * 2
result = ''
language = input('Укажите язык рус/eng: ')
alphabet = alphabet_eng if language == 'eng' else alphabet_ru

if language != 'eng' and language != 'рус':
    print('Указан неверный язык ввода, начните игру заново!')
    sys.exit()

for n in text:
    position = alphabet.find(n)
    new_position = position + number
    if n in alphabet:
        result += alphabet[new_position]
    else:
        result += n

print(f'Результат шифрования: {result}')
