#Программа для уточнения корней методом касательных.

#Леонов Владислав
#ИУ7-16Б

import math

#Вычисление значения функции в точке
def function(x):
    function_value = x*x-4
    return function_value

#Вычисление значения производной в точке
def derivative(x):
    derivative_value = 2*x
    return derivative_value

#Функция для проверки исходных данных
def check_input(x,a = False):
    try: x = float(x)
    except ValueError:
        print('Некорректные данные, повторите ввод: ')
        return False
    if x <= a and a != False:
        print('Конец отрезка должен быть больше начала, повторите ввод: ')
        return False
    return True

print('Вас приветствует программа для уточнения корней\n\
методом касательных на заданном отрезке\n')

#Ввод начала отрезка с проверкой корректности
start = input('Введите начало отрезка: ')
while not check_input(start):
    start = input()
start = float(start)

#Ввод конца отрезка с проверкой корректности
stop = input('Введите конец отрезка: ')
while not check_input(stop,start):
    stop = input()
stop = float(stop)

#Ввод шага с проверкой корректности
step = input('Введите шаг: ')
while not check_input(step):
    step = input()
step = float(step)

#Ввод точности для вычисления с проверкой корректности
acc = input('Введите точность: ')
while not check_input(acc):
    acc = input()
acc = float(acc)


#Максимальное число итераций для метода Ньютона
max_iterations = 1e5

check = 0
roots = []

x_l = start
i = 1
while x_l < stop:
    x_r = x_l + step
    if x_r > stop: x_r = stop
    
    #Проверка разности знаков на концах рассматриваемого отрезка
    if function(x_l) * function(x_r) < 0:

        if check == 0:
            print('┌'+14*'─'+'┬'+20*'─'+'┬'+14*'─'+'┬'+14*'─'+'┬'+19*'─'+'┬'+13*'─'+'┐')
            print('│{:<14}│{:<20}│{:<14}│{:<14}│{:<19}│{:<13}│'.format('№ интервала',\
            'Границы интервала','Значение корня','Значение f(x)','Кол-во итераций',\
            'Код ошибки'))
            check = 1

        print('├'+14*'─'+'┼'+20*'─'+'┼'+14*'─'+'┼'+14*'─'+'┼'+19*'─'+'┼'+13*'─'+'┤')
        root = x_l
        prev_point = root + 10 * acc
        num_of_iterations = 0
        error_code = '-'

        while abs(root - prev_point) >= acc and\
              num_of_iterations < max_iterations:

            #Проверка существования производной
            try:
                derivative(root)
            except:
                error_code = '1'
                break

            #Проверка нулевой производной
            if derivative(root) == 0:
                error_code = '2'
                break

            #Новое значение приближения при помощи касательной
            prev_point = root
            root = root - function(root)/derivative(root)
            num_of_iterations += 1

        #Печать информации в зависиости от возникновения ошибки
        if error_code == '-':
            print('│{:<14}│[{:^8.2g};{:^9.2g}]│{:<14.2g}│{:<14.2g}│{:<19}│{:<13}│'.format(i,\
x_l,x_r, root,function(root),num_of_iterations,error_code))
            roots.append(root)
        else:
            print('│{:<14}│[{:^8.2g};{:^9.2g}]│{:<14.2}│{:<14.2}│{:<19}│{:<13}│'.format(i,\
x_l,x_r, '-','-','-',error_code))

    #Если корень попадает на границу отрезка
    elif function(x_l) * function(x_r) == 0:

        if check == 0:
            print('┌'+14*'─'+'┬'+20*'─'+'┬'+14*'─'+'┬'+14*'─'+'┬'+19*'─'+'┬'+13*'─'+'┐')
            print('│{:<14}│{:<20}│{:<14}│{:<14}│{:<19}│{:<13}│'.format('№ интервала',\
            'Границы интервала','Значение корня','Значение f(x)','Кол-во итераций',\
            'Код ошибки'))
            check = 1

        error_code = '3'
        if function(x_l) == 0:
            root = x_l
        else:
            root = x_r
        if root not in roots:
            print('├'+14*'─'+'┼'+20*'─'+'┼'+14*'─'+'┼'+14*'─'+'┼'+19*'─'+'┼'+13*'─'+'┤')
            print('│{:<14}│[{:^8.2g};{:^9.2g}]│{:<14.2g}│{:<14.2g}│{:<19}│{:<13}│'.format(i,\
x_l,x_r, root,function(root),'-',error_code))
            roots.append(root)
            
    x_l += step
    i += 1

if check == 1:
    print('└'+14*'─'+'┴'+20*'─'+'┴'+14*'─'+'┴'+14*'─'+'┴'+19*'─'+'┴'+13*'─'+'┘')
    #Печать расшифровки ошибок
    print('''Коды ошибок:
1 - Производная не существует;
2 - Производная равна нулю;
3 - Корень находится на границе интервала.''')
else:
    print('\nНа заданном отрезке корни отсутствуют')
        
        
                  

            

            
        
    
            
            
    
        
