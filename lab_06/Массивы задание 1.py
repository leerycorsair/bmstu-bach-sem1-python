#Программа для работы с массивом
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

m = []
n = int(input('Введите количество чисел в массиве: '))
i = 0
num_of_pos = num_of_neg = 0
#Проверка реалистичности введенных данных
if n > 0:
    #Ввод числового массива с проверкой данных
    print('Вводите числа, каждое в отдельной строке')
    while i != n:
        num = input()
        check = str_to_num_check(num)
        while check == False:
            print ('Вы ввели число с ошибкой, попробуйте снова')
            num = input()
            check = str_to_num_check(num)
        num = float(num)
        if num >= 0:
            num_of_pos += 1
        else:
            num_of_neg += 1
        m.append(num)
        i += 1

    #Печать исходного массива
    print()
    print('Исходный массив:')
    print(m)

    #Сортировка массива с чередованием знака
    if num_of_pos >= num_of_neg:
        for i in range(len(m)-1):
            if i % 2 == 0:
                if m[i]<0:
                    for j in range(len(m)-1,i,-1):
                        if m[j]>=0: m[i],m[j] = m[j],m[i]
            else:
                if m[i]>=0:
                    for j in range(len(m)-1,i,-1):
                        if m[j]<=0: m[i],m[j] = m[j],m[i]
    else:
        for i in range(len(m)-1):
            if i % 2 == 0:
                if m[i]>=0:
                    for j in range(len(m)-1,i,-1):
                        if m[j]<=0: m[i],m[j] = m[j],m[i]
            else:
                if m[i]<0:
                    for j in range(len(m)-1,i,-1):
                        if m[j]>=0: m[i],m[j] = m[j],m[i]

    #Печать преобразованного массива
    print()
    print('Массив после выполнения программы')
    print(m)
else:
    print('Количество чисел в массиве не может быть меньше или равно 0')
