#Программа для вычисления значения функции
#Выполнил: Леонов Владислав
#ИУ7-16Б
x = float(input('Введите x: ')) # Ввод аргумента
if x < -1: #Проверка аргумента
    y = -1
elif -1 < x < 2:#Проверка аргумента
    y = -abs(x-1) + 1
else:
    y = 0
print (' y = ', y) #Вывод ответа
