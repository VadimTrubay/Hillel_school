# Дан многомерный список в котором находится результат игры в крестики нолики,
# выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
# Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

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
            print('Victory player 1!')
            exit()

        else:
            print('draw')
        exit()
        # if a[i][0] == a[i][1] == a[i][2]:
        #     print('Victory player 1!')
        #     break
        # else:
        #     print('Victory player 2!')