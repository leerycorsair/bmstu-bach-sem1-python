import math

def function(x):
    return math.cos(x)

x_l = float(input('Введите начало отрезка: '))
x_r = float(input('Введите конец отрезка: '))
acc = float(input('Введите точность: '))

while abs(x_l - x_r) > acc:

    x = (x_l + x_r) / 2

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
