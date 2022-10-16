# Напишите функцию read_last(lines, file), которая будет открывать определенный
# файл file и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).

def read_last(lines, file):
    if lines > 0:
        with open(file, 'r') as f:
            file_lines = f.readlines()[-lines:]
        for i in file_lines:
            print(i.strip())
    else:
        print('Error is not a positive integer')


read_last(3, 'text.txt')
