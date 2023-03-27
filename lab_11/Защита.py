import math

def function(x):
    return x*x -4

x_l = float(input('Введите начало отрезка: '))
x_r = float(input('Введите конец отрезка: '))
acc = float(input('Введите точность: '))

while abs(x_l - x_r) > acc:

    x = x_l - (x_r - x_l)/(function(x_r)-function(x_l))*function(x_l)

    if function(x_l)*function(x) < 0:
        x_r = x
    elif function(x_r)*function(x) < 0:
        x_l = x

    elif function(x_l)*function(x) == 0:
        if function(x_l) == 0:
            x = x_l
        break

    elif function(x_r)*function(x) == 0:
        if function(x_r) == 0:
            x = x_r
        break
            

print ('Корень уравнения на заданном отрезке:','{:<5.2f}'.format(x))
