# Программа для вычисления определенного интеграла методами трапеций
# и параболы и нахождения числа разбиений для менее точного метода
# для заданной пользователем точности

#Выполнил Леонов Владислав
#ИУ7-16Б

import math
#Является ли введенная строка float-числом?
def str_to_float_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

#Является ли введенная строка int_pos-числом?
def str_to_int_check(y):
    for i in range (len(y)):
        if y[i]<'0' or y[i]>'9': return False
    return True

#Значение функции
def func(x):
    y = x**2 #math.sin(x)+ 0.5/ math.sqrt(x)
    return y

#Первообразная функции
def prim(x):
    prim_value = x**3/3 #math. cos(x) + math.sqrt(x)
    return prim_value

#Площадь методом парабол:
def parab(a, b, n):
    if n%2!=0:return '---'
    h = (b-a)/n
    summ = 0
    for i in range (n+1):
        if not i % n: k = 1
        elif i % 2: k = 4
        else: k = 2
        summ += k* func(a+i*h)
    summ *= h/3
    return summ

#Площадь методом трапеций:
def trapez(a, b, n):
    h = (b-a)/n
    summ = 0
    for i in range (n+1):
        if not i % n: k = 1
        else: k = 2
        summ += k* func(a+i*h)
    summ *= h/2
    return summ

#Ввод исходных данных с проверкой на их корректность
a = input('Ввведите начало отрезка интегрирования: ')
check = str_to_float_check(a)
while check != True:
    a = input('Вы ввели начало с ошибкой, повторите ввод: ')
    check = str_to_float_check(a)
a = float(a)

b = input('Ввведите конец отрезка интегрирования: ')
check = False
while check != True:
    check = str_to_float_check(b)
    if check == False:
        b = input('Вы ввели конец с ошибкой, повторите ввод: ')
        check = str_to_float_check(b)
    if check:
        if float(b)<a:
            check = False
            b = input ('Число b должно быть больше a, повторите ввод: ')
b = float(b)

n = input('Введите два числа разбиения через пробел: '). split()
while len(n)!=2:
    n = input('Вы ввели не два числа, повторите ввод: ').split()
for i in range (len(n)):
    check = False
    while check != True:
        check = str_to_int_check(n[i])
        if check == False:
            print('Вы ввели число с ошибкой (', n[i], ') повторите ввод этого числа: ', sep='')
            n[i] = input()
            check = str_to_int_check(n[i])
    n[i] = int(n[i])

#Вывод таблицы значений интегралов
print('\n\n\n')
print('Площадь, вычисленная методами параболы и трапеции:')
print('┌'+'─'*20+'┬'+'─'*41+'┐')
print('|'+' '*20+'|'+'             Число разбиений             '+'|')
print('|'+' '*20+'├'+'─'*20+'┬'+'─'*20+'┤')
print('|'+' '*20+'|','{:^20}'.format(n[0]),'|', '{:^20}'.format(n[1]),'|', sep = '')
print('├'+'─'*20+'┼'+'─'*20+'┼'+'─'*20+'┤')
print('|  Метод трапеций    |','{:^20.5}'.format(trapez(a,b,n[0])),'|', '{:^20.5}'.format(trapez(a,b,n[1])),'|', sep = '')
print('├'+'─'*20+'┼'+'─'*20+'┼'+'─'*20+'┤')
print('|  Метод парабол     |','{:^20.5}'.format(parab(a,b,n[0])),'|', '{:^20.5}'.format(parab(a,b,n[1])),'|', sep = '')
print('└'+'─'*20+'┴'+'─'*20+'┴'+'─'*20+'┘')

#Вычисление количества разбиений для менее точного метода, если такой имеется, для заданной точности
s_t = prim (b) - prim (a)
if n[0]%2!=0 or n[1]%2!=0:
    if abs(trapez(a,b,n[1])- s_t ) < 1e-10 and abs(parab(a,b,n[1]) - s_t) < 1e-10:
        print ('Оба метода точны')
    else:
        eps = float(input('Введите точность для менее точного метода: '))
        n = 2
        if abs(trapez(a,b,n)-s_t) - abs(parab(a,b,n)-s_t) > 0:
            while abs(trapez(a,b,n) -trapez(a,b,n-1)) > eps: n += 1
            print('Для заданной точности для метода трапеций требуется', n , 'разбиений')
            print('Итоговое значение интеграла: ', '{:^10.5}'.format(trapez(a,b,n)))
        else:
            while abs(parab(a,b,n) - parab(a,b,n-1))> eps: n += 1
            print('Для заданной точности для метода парабол требуется', n, 'разбиений')
            print('Итоговое значение интеграла: ', '{:^10.5}'.format(parab(a,b,n)))
