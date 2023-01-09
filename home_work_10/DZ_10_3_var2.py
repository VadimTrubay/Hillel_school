# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

print('Is this game X or 0!')
print('Enter symbols X or 0 according to the scheme\n\n'
      'num_1|num_2|num_3\n'
      '-----------------\n'
      'num_4|num_5|num_6\n'
      '-----------------\n'
      'num_7|num_8|num_9\n\n')

a = []
h = 1
for _ in range(3):
    b = []
    for n in range(3):
        number = str(input(f'num_{h}: '))
        h += 1
        b.append(number)
        if number != '0' and number != 'x':
            print('Error: invalid symbol, restart the game!', end='\n\n')
            exit(4)
    a.append(b)
print(a[0], end='\n')
print(a[1], end='\n')
print(a[2], end='\n')

for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        if a[0][0] == a[0][1] == a[0][2] == '0' or \
                a[1][0] == a[1][1] == a[1][2] == '0' or \
                a[2][0] == a[2][1] == a[2][2] == '0' or \
                a[0][0] == a[1][0] == a[2][0] == '0' or \
                a[0][1] == a[1][1] == a[2][1] == '0' or \
                a[0][2] == a[1][2] == a[2][2] == '0' or \
                a[0][0] == a[1][1] == a[2][2] == '0' or \
                a[0][2] == a[1][1] == a[2][0] == '0':
            print('Victory player 0!')
            exit()
        elif a[0][0] == a[0][1] == a[0][2] == 'x' or \
                a[1][0] == a[1][1] == a[1][2] == 'x' or \
                a[2][0] == a[2][1] == a[2][2] == 'x' or \
                a[0][0] == a[1][0] == a[2][0] == 'x' or \
                a[0][1] == a[1][1] == a[2][1] == 'x' or \
                a[0][2] == a[1][2] == a[2][2] == 'x' or \
                a[0][0] == a[1][1] == a[2][2] == 'x' or \
                a[0][2] == a[1][1] == a[2][0] == 'x':
            print('Victory player x!')
            exit()
        else:
            print('Draw!')
        exit()