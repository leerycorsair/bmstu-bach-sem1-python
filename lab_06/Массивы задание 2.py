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
num_of_pos = 0
index_of_neg = -1

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
        m.append(num)
        i += 1

    #Печать исходного массива
    print()
    print('Исходный массив:')
    print(m)

    #Подсчет положительных чисел, кратных,  5 и поиск индекса последнего отрицательного
    for i in range(len(m)):
        if m[i] > 0 and (i+1) % 5 == 0:
            num_of_pos += 1
        if m[i] < 0:
            index_of_neg = i

    #Печать преобразованного массива
    print()
    if index_of_neg == -1:
        print(m)
        print ('Отрицательных чисел нет в массиве')
    if num_of_pos > 0 and index_of_neg != -1:
        m[index_of_neg] = num_of_pos
        print('Преобразованный массив:')
        print(m)
    else:
        print('Массив остался без изменений')
        print(m)

    print('Число положительных чисел в массиве, позиция которых кратна 5:',num_of_pos)

else:
    print('Количество чисел в массиве не может быть меньше или равно 0')
