# Задание 5:
"""Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре
со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее. Нужно реализовать шифрование
с помощью Python.
Пользователь вводит строку которую хочет зашифровать и число (сдвиг), нужно с помощью шифра Цезаря ее
зашифровать и вывести на экран.
Выполнить задание нужно с помощью цикла for и строк, для получения числового представления символа
можно использовать ord, а для преобразования числа в строку - chr."""

text = input('Шифр-машина Цезаря готова к работе\nВведите текст: ').lower()
number = int(input('Введите количество символов сдвига(цифра): '))
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_eng = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
result = ''
language = input('Выберите язык ru/eng: ')

if language == 'ru':
    for i in text:
        position = alphabet_ru.find(i)
        new_position = position + number
        if i in alphabet_ru:
            result += alphabet_ru[new_position]
        else:
            result += i
    print(f'Результат шифрования: {result}')
else:
    for i in text:
        position = alphabet_eng.find(i)
        new_position = position + number
        if i in alphabet_eng:
            result += alphabet_eng[new_position]
        else:
            result += i
    print(f'Результат шифрования: {result}')
