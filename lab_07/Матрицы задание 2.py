#Программа для  определения соединенных пунктов, образующих треугольники

#Выполнил Леонов Владислав
#ИУ7-16Б

#Функция для обеспечения правильности вводимых данных
def num_check(x):
    return x == '0' or x=='1'

#Ввод исходного массива
n = int(input('Введите размер матрицы NB: '))
NB = []
st = []
print ('Вводите строки матрицы, разделяя элементы пробелами, элементы равны либо 1 либо 0')
for i in range(n):
    row = input().split()
    while len(st)!= n:
        for j in range(len(row)):
            check = num_check(row[j])
            while check == False:
                print ('Вы ввели элемент с ошибкой (\'', row[j], '\'), повторите ввод: ', sep = '', end = '')
                row[j] = input()
                check = num_check(row[j])
            st.append(int(row[j]))
        if len(st)!= n:
            row = input('Вы ввели строку с ошибкой, число элементов не соответствует размеру матрицы, повторите ввод: ').split()
            st = []
    NB.append(st)
    st = []

#Обработка массива
KT = []
str_num = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if NB[i][j] == 1:
            for k in range(j+1,n):
                if NB[i][k] == 1 and NB[j][k] == 1:
                    KT.append(str(i+1)+str(j+1)+str(k+1))


#Вывод массива с тройками соединенных пунктов
print('Тройки пунктов, которые соединены отрезками и образуют треугольники:')
for i in range(len(KT)):
    print(KT[i])
