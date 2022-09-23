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
language = input('Укажите язык рус/eng: ')
result = ''

if language == 'рус':
    if language == 'eng':
        print('Ошибка, Вы не правильно указали язык ввода! ')
    for n in text:
        position = alphabet_ru.find(n)
        new_position = position + number
        if n in alphabet_ru:
            result += alphabet_ru[new_position]
        else:
            result += n
    print(f'Результат шифрования: {result}')

elif language == 'eng':
    if language == 'рус':
        print('Ошибка, Вы не правильно указали язык ввода! ')
    for n in text:
        position = alphabet_eng.find(n)
        new_position = position + number
        if n in alphabet_eng:
            result += alphabet_eng[new_position]
        else:
            result += n
    print(f'Результат шифрования: {result}')
elif language != 'рус' or language != 'eng':
    print('Ошибка, Вы не указали язык ввода! ')
else:
    print('До скорой встречи!')
