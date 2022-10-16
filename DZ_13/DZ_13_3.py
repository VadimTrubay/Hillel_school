# Напишите функцию sum_range(start, end), которая суммирует все
# целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sun_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))
