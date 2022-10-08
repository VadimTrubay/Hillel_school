# Задание #1:
# Дано два множества A и B
# В множестве А находятся имена должников за Сентябрь
# В множестве B находятся имена должников за Октябрь
# Найти:
# * Вывести имена людей которые должны за Сентябрь и Октябрь
# * Вывести должников за Октябрь у которых нет долга за Сентябрь

A_debtors_sept = {"vasia", "petia", "kolia", "sasha", "vadim", "misha"}
B_debtors_okt = {"vasia", "tima", "kolia", "galia", "fedia", "platon", "misha"}

print(f'debtors september and oktober = {A_debtors_sept.intersection(B_debtors_okt)}')
print(f'debtors only for october = {B_debtors_okt.difference(A_debtors_sept)}')
