a = [
    [1, 6, 8, 5, 4, 0, 3],
    [5, 7, 8, 9, 4, 2, 1],
    [6, 0, 7, 8, 1, 2, 5],
    [5, 7, 2, 7, 5, 2, 1]
    ]
for x, x_value in enumerate(a):
    print()
    for y, y_value in enumerate(x_value):
        if y % 2 == 0:
            print(y_value, end=' ')
        # if y > x:
        #     print(y, end=' ')