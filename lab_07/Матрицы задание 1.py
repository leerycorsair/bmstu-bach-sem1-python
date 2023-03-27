#Программа для  вычисления средего арифмитического отриц. эллементов каждой
#строки матрицы R и записи результатов в отдельный массив

#Выполнил Леонов Владислав
#ИУ7-16Б

#Функция, чтобы проверить, является ли введенная строка числом
def str_to_num_check(x):
    dot_check = 0
    e_check = 0
    plus_minus_check = 0
    if x =='': return False
    x = ' ' + x
    for i in range(1,len(x)):
        if (x[i]>'9' or x[i]<'0') and x[i]!='+' and x[i]!='-' and x[i]!='e'and x[i]!='.' and x[i]!='E': return False
        if x[i]=='.':
            dot_check += 1
        if x[i]=='+' or x[i]=='-':
            plus_minus_check += 1
        if x[i]=='e' or x[i]=='E':
            e_check += 1
        if dot_check > 1 or e_check > 1: return False
        if plus_minus_check > 1 and e_check == 0: return False
        if x[i] == '.' and e_check == 1: return False
        if (x[i] == '+' or x[i] == '-') and dot_check == 1 and e_check == 0: return False
        if (x[i] == '+' or x[i] == '-') and ('0'<=x[i-1]<='9' or x[i-1]=='.'): return False
    if (x[1] == '+' or x[1] == '-') and (x[2] == 'e' or x[2] == 'E'): return False
    if x[1] == 'e' or x[1] == 'E': return False
    if x == '.': return False
    if x[len(x)-1] == 'e' or x[len(x)-1] == 'E' or x[len(x)-1] == '-' or x[len(x)-1] == '+' :return False
    return True

#Ввод исходного массива
num_of_row = int(input('Введите число строк матрицы NB: '))
el_per_row = int(input('Введите число элементов в строке матрицы NB: '))
R = []
st = []
print ('Вводите строки матрицы, разделяя элементы пробелами')
for i in range(num_of_row):
    row = input().split()
    while len(st)!= el_per_row:
        for j in range(len(row)):
            check = str_to_num_check(row[j])
            while check == False:
                print ('Вы ввели элемент с ошибкой (\'', row[j], '\'), повторите ввод: ', sep = '', end = '')
                row[j] = input()
                check = str_to_num_check(row[j])
            st.append(float(row[j]))
        if len(st)!= el_per_row:
            row = input('Вы ввели строку с ошибкой, число элементов не соответствует размеру матрицы, повторите ввод: ').split()
            st = []
    R.append(st)
    st = []

# Вычисление среднего арифимитического строк матрицы
V = []
for i in range (num_of_row):
    Arif_mean = 0
    k = 0
    for j in range (el_per_row):
        if R[i][j] < 0:
            Arif_mean += R[i][j]
            k += 1
    if k > 0:
        Arif_mean = Arif_mean/k
        V.append(Arif_mean)

#Поиск наименьшего среднего арифмитического и обмен местами с первым элементом
i_min = 0
for i in range(len(V)):
    if V[i] < V[i_min]:
        i_min = i
if len(V)>0:
    V[i_min], V[0] = V[0], V[i_min]

#Вывод матрицы и массива
print()
print('Матрица R: ')
for i in range (num_of_row):
    for j in range (el_per_row):
        print('{:>8.3}'.format(R[i][j]), end=' ')
    print()
if len(V)>0:
    print('Массив V со средним арифм. отрицательных элементов строк: ')
    for k in range (len(V)):
        print('{:>8.3}'.format(V[k]), end=' ')
else:
    print ('В данном массиве отсутствуют отрицательные элементы')
