# Задание #2:
# Права доступа
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

# x = ['W', 'R', 'X', 'WR', 'WX', 'RX', 'WRX']

i = 0
n = int(input('Enter number of files >: '))
if i <= n:
    for i in range(n):
        string_file = input('Enter a string with the file name and allowed operations >: ')
        d = [string_file]
        for s in range(len(d)):
            print(d[s])
            for n in range(len(d[s])):
                # print(d[s][n])
                if d[s][n] == 'W':
                    print('W')
                elif d[s][n] == 'R':
                    print('R')
                elif d[s][n] == 'X':
                    print('X')
                elif d[s][n] == 'W R':
                    print('W R')
                elif d[s][n] == 'W X':
                    print('W X')
                elif d[s][n] == 'R X':
                    print('R X')
                elif d[s][n] == 'W R X':
                    print('W R X')
        print(d)

# d_rec = []
# j = 0
# m = int(input('Enter number of file requests >: '))
# if j <= m:
#     for j in range(m):
#         string_file = input(f'Enter request {j+1} >: ')
#         d_rec.append(string_file)
# a = dict(s.split(' ') for s in d_rec)
# # print('W' in d)
# print(d_rec)
# print(a)


# d = ['python.exe X R', 'book.txt W ', 'notebook.exe ']
# for s in range(len(d)):
#     # print(d[s])
#     for n in range(len(d[s])):
#         # print(d[s][n])
#         if d[s][n] == 'W':
#             print('W')
#         elif d[s][n] == 'R':
#             print('R')
#         elif d[s][n] == 'X':
#             print('X')
#         elif d[s][n] == 'W R':
#             print('W R')
#         elif d[s][n] == 'W X':
#             print('W X')
#         elif d[s][n] == 'R X':
#             print('R X')
#         elif d[s][n] == 'W R X':
#             print('W R X')


