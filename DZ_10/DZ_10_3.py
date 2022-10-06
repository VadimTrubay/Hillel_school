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
        number = int(input(f'Enter number num_{h}: '))
        h += 1
        b.append(number)
    a.append(b)

for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        if a[0][0] == a[0][1] == a[0][2] == 0 or \
                a[1][0] == a[1][1] == a[1][2] == 0 or \
                a[2][0] == a[2][1] == a[2][2] == 0 or \
                a[0][0] == a[1][0] == a[2][0] == 0 or \
                a[0][1] == a[1][1] == a[2][1] == 0 or \
                a[0][2] == a[1][2] == a[2][2] == 0 or \
                a[0][0] == a[1][1] == a[2][2] == 0 or \
                a[0][2] == a[1][1] == a[2][0] == 0:
            print('Victory player 0!')
            exit()
        elif a[0][0] == a[0][1] == a[0][2] == 1 or \
                a[1][0] == a[1][1] == a[1][2] == 1 or \
                a[2][0] == a[2][1] == a[2][2] == 1 or \
                a[0][0] == a[1][0] == a[2][0] == 1 or \
                a[0][1] == a[1][1] == a[2][1] == 1 or \
                a[0][2] == a[1][2] == a[2][2] == 1 or \
                a[0][0] == a[1][1] == a[2][2] == 1 or \
                a[0][2] == a[1][1] == a[2][0] == 1:
            print('Victory player 1!')
            exit()

        else:
            print('Draw!')
        exit()
