# Задание #1:
# Дано два множества A и B
# В множестве А находятся имена должников за Сентябрь
# В множестве B находятся имена должников за Октябрь
# Найти:
# * Вывести имена людей которые должны за Сентябрь и Октябрь
# * Вывести должников за Октябрь у которых нет долга за Сентябрь

A_debtors_sept = {"1", "2", "3", "5", "6", "8"}
B_debtors_okt = {"2", "3", "6", "9", "10", "11", "12"}

print(f'debtors september and oktober = {A_debtors_sept.union(B_debtors_okt)}')
print(f'debtors only for october = {B_debtors_okt.difference(A_debtors_sept)}')
