# Задание 2:
# Пользователь вводит текст и слово которое нужно найти,
# если это слово есть в тексте, вывести 'YES', иначе 'NO'

text = input('Enter text >: ')
wd = input('Enter a search term >: ')

new_text = text.split()

if wd not in new_text:
    print('NO')
    exit(4)

if new_text.index(wd) != -1:
    print('YES')
