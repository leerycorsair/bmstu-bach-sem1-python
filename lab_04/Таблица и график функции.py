#Программа для вывода значений функции в виде таблицы, а также ее графика
#Выполнил Леонов Владислав
#ИУ7-16Б
import math
print('Вас приветствует программа для вывода значений функций:')
print('y1 = a**3 - 23,8*a**2 + 44,9*a - 10,34')
print('y2 = a*ln(a)-6')
print('Также программа находит разность между макс. значением y1 и y2')
eps = 1e-6
#Ввод начала, конца отрезка и шага
a1 = float(input('Введите начало отрезка необходимых значений: '))
a2 = float(input('Введите конец отрезка необходимых значений(конец больше начала): '))
sh = float(input('Введите шаг(больше 0): '))
a10 = a1
#Максимальные значения функций
y1max = a1**3 - 23.8*a1**2 + 44.9*a1 - 10.34
y1min = a1**3 - 23.8*a1**2 + 44.9*a1 - 10.34
y2max = -7
#Проверка верности входных данных
if a2 < a1 or sh == 0 or sh < 0:
    print('Входные данные неверные')
else:
    print()
    print()
    print()
    print('Таблица значений функций')
#Вывод таблицы
    print('┌'+'─'*15+'┬'+'─'*16+'┬'+'─'*16+'┐')
    print('│'+' '*7+'A'+' '*7+'│'+' '*7+'Y1'+' '*7+'│'+' '*7+'Y2'+' '*7+'│')
#Вычисление числа итераций
    num=int((a2-a1+eps)//sh)
    for k in range(num+1):
        y1 = a1**3 - 23.8*a1**2 + 44.9*a1 - 10.34
#Проверка максимального значения
        if y1 > y1max:
            y1max = y1
#Проверка минимального значения
        if y1 < y1min:
            y1min = y1
#Проверка существования второй функции и проверка ее максимального значения
        if a1>0:
            y2 = a1*math.log(a1) - 6
            if y2>y2max:
                y2max = y2
        else:
            y2 = 'не сущ'
#Вывод таблицы
        print(('├'+'─'*15+'┼'+'─'*16+'┼'+'─'*16+'┤'))
        print('│ {:^13.6} │ {:^14.6} │ {:^14.6} │'.format(a1, y1,y2))
        a1 += sh
    if a1-a2-sh+eps<0:
        y1 = a2 ** 3 - 23.8 * a2 ** 2 + 44.9 * a2 - 10.34
        if a2 > 0:
            y2 = a1 * math.log(a1) - 6
            if y2 > y2max:
                y2max = y2
        else:
            y2 = 'не сущ'
        print(('├' + '─' * 15 + '┼' + '─' * 16 + '┼' + '─' * 16 + '┤'))
        print('│ {:^13.6} │ {:^14.6} │ {:^14.6} │'.format(a2, y1,y2))
#Вывод последней строки
    print('└'+'─'*15+'┴'+'─'*16+'┴'+'─'*16+'┘')
#В случае существования второй функции, вывод модуля разности между функциями
    if y2max!=-7 and y2!='не сущ':
        r = abs(y1max - y2max)
        print ('Модуль разности между максимальными значениями y1 и y2: ','{:4.3}'.format(r) )
    print()
    print()
    print()
    print('График функции Y1')
    z = int(input('Введите число засечек по оси OY(от 4 до 8): '))
    if 3<z<9:
#Шаг для засечек
        if z==4 or z==5 or z==6:
            ser = 60
        else:
            ser = 84
        sh0 = (y1max - y1min)/(z-1)
        y1min0 = y1min
        print (8*' ',end='')
#Вывод значений оси OY и OX в зависимости от числа засечек
        while y1min0 < y1max - sh0 + eps:
            print('{:>4.2e}'.format(y1min0), end=(' ' *int(ser/(z-1) - 9)))
            y1min0 += sh0
        print ('{:>4.2e}'.format(y1max))
        print (13 * ' ', '┌', ('─' * (int(ser/ (z - 1)) - 1)+ '┬') * (z - 2), '─' * (int(ser / (z - 1)) - 1), '┐', sep='')
        for k in range(num+1):
            y1 = a10 ** 3 - 23.8 * a10 ** 2 + 44.9 * a10 - 10.34
            if y1max > 0 and y1min < 0:
                space_fuction = int((y1-y1min+eps)/(y1max-y1min)*ser)
                space_liney = int((0-y1min+eps)/(y1max-y1min)*ser)
                if space_fuction == space_liney:
                    print('{:^13.6}'.format(a10),space_fuction*' ', '*', sep='')
                elif space_fuction - space_liney< eps:
                    print('{:^13.6}'.format(a10), space_fuction*' ', '*',
                            (space_liney-space_fuction-1)*' ','│',sep='')
                elif space_fuction>space_liney:
                    print('{:^13.6}'.format(a10), space_liney * ' ', '│',
                            (space_fuction - space_liney-1) * ' ', '*', sep='')
                a10 += sh
            else:
                print('{:^13.6}'.format(a10),space_fuction*' ', '*', sep='')
    else:
        print('Вы ввели неверное количество засечек')