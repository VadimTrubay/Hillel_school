# Напишите функцию change(lst), которая принимает список и меняет местами его первый
# и последний элемент.
# В исходном списке минимум 2 элемента.

def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("Error: not enough list items")
    return lst


print(change([1, 2, 3, 4, 5, 6]))
