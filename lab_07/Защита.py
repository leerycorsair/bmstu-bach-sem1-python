num_of_rows = int(input('Введите количество строк матрицы: '))
el_per_row = int(input('Введите количество элементов в строке: '))

M = []
am = []
s = k = 0.0
print('Вводите строки матрицы, разделяя элементы пробелом')
for i in range(num_of_rows):
    row = input().split()
    for j in range (el_per_row):
        row[j] = float(row[j])
    M.append(row)

print('Исходная матрица')
for i  in range(num_of_rows):
    for j in range(el_per_row):
        print('{:4.3}'.format(M[i][j]), end = ' ')
    print()
    
for i in range(el_per_row):
    for j in range (num_of_rows):
        if M[j][i] > 0:
            s += M[j][i]
            k += 1
    if k > 0:
        s = s/k
    am. append(s)
    s = k = 0.0

i_min = 0
for i in range (el_per_row):
    if am[i]<am[i_min] and am[i] != 0:
        i_min = i

if max(am)>0:
    for i in range(num_of_rows):
        del(M[i][i_min])
    print('Преобразованная матрица')
    for i in range(num_of_rows):
        for j in range(el_per_row-1):
            print('{:4.3}'.format(M[i][j]), end = ' ')
        print()
else:
    print ('В исходном массиве отсутствуют положительные элементы')
