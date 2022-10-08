A_debtors_sept = {"vasia", "petia", "kolia"}
B_debtors_okt = {"oleg", "sasha", "misha"}
C_all = A_debtors_sept.union(B_debtors_okt)

print(f'debtors september and oktober = {C_all}')
