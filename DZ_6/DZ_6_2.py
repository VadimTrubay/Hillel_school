#Вывести треугольник #1 с шириной N с помощью цикла while
# *
# **
# ***
# ****
# *****

N = int(input('Enter N>: '))
h = 1
while h <= N:
    print(h * "*")
    h = h + 1
