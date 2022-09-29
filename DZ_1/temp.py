# input_number = 1
# A = []
# B = int(input(f'Enter number N >: '))
# for i in range(0, B):
#     A.append(int(input(f'Enter number {input_number} >: ')))
#     input_number += 1
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

min_value = A[0]
max_value = 0
for j in A:
    if j > max_value:
        max_value = j
    if j < min_value:
        min_value = j
print(min_value, max_value)


    # n = int(input())
    # if max_number is None or n > max_number:
    #     max_number = n
# print(max_number)