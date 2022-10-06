# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

print('Is this game X or 0!')
print('Enter symbols X or 0 according to the scheme\n\n'
      '1 | 2 | 3 \n'
      '---------\n'
      '4 | 5 | 6 \n'
      '---------\n'
      '7 | 8 | 9 \n')

n = 3
m = 3
a = [['-'] * m for i in range(n)]
h = 0


def my_print():
    print(a[0])
    print(a[1])
    print(a[2])


for i in range(0, 9):
    value = input('Enter symbol(only x or 0)>: ')
    cell_number = int(input('Enter cell number>: '))
    if cell_number == 1:
        a[0][0] = value
        my_print()
    if cell_number == 2:
        a[0][1] = value
        my_print()
    if cell_number == 3:
        a[0][2] = value
        my_print()
    if cell_number == 4:
        a[1][0] = value
        my_print()
    if cell_number == 5:
        a[1][1] = value
        my_print()
    if cell_number == 6:
        a[1][2] = value
        my_print()
    if cell_number == 7:
        a[2][0] = value
        my_print()
    if cell_number == 8:
        a[2][1] = value
        my_print()
    if cell_number == 9:
        a[2][2] = value
        my_print()

    zero = a[0][0] == a[0][1] == a[0][2] == '0' or \
           a[1][0] == a[1][1] == a[1][2] == '0' or \
           a[2][0] == a[2][1] == a[2][2] == '0' or \
           a[0][0] == a[1][0] == a[2][0] == '0' or \
           a[0][1] == a[1][1] == a[2][1] == '0' or \
           a[0][2] == a[1][2] == a[2][2] == '0' or \
           a[0][0] == a[1][1] == a[2][2] == '0' or \
           a[0][2] == a[1][1] == a[2][0] == '0'

    if zero:
        print()
        print('VICTORY PLAYER "0"!')
        exit()

    xero = a[0][0] == a[0][1] == a[0][2] == 'x' or \
           a[1][0] == a[1][1] == a[1][2] == 'x' or \
           a[2][0] == a[2][1] == a[2][2] == 'x' or \
           a[0][0] == a[1][0] == a[2][0] == 'x' or \
           a[0][1] == a[1][1] == a[2][1] == 'x' or \
           a[0][2] == a[1][2] == a[2][2] == 'x' or \
           a[0][0] == a[1][1] == a[2][2] == 'x' or \
           a[0][2] == a[1][1] == a[2][0] == 'x'

    if xero:
        print()
        print('VICTORY PLAYER "X"!')
        exit()
    if i >= 8:
        print()
        print('DRAW!')
