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

action = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file = {}
for i in range(int(input('Enter number of files(digit) >: '))):
    name, *operations = input(f'Enter a string with the file name and allowed operations {i+1}>: ').split()
    file[name] = set(operations)

for j in range(int(input('Enter number of file requests(digit) >: '))):
    request, name = input(f'Enter request {j+1}>: ').split()
    if action[request] in file[name]:
        print('OK')
    else:
        print('Access denied')
