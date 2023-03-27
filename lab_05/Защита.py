x = float(input('Введите x: '))
eps = float(input('Введите точность: '))
n = 4
s = 0
it = 1
curr = -2*2*x*x / (n-3) / (n-2)
nxt = -curr*2*2*x*x / (n-1) / n
print()
while abs(nxt) > eps:
    s += curr
    it += 1
    curr = nxt
    n += 2
    nxt = -curr*2*2*x*x / (n-1) / n
print(it)
print('Сумма ряда с относительно низкой точностью = ', '{:5.4}'.format(s))
print('Сумма ряда с относительно высокой точностью = ', '{:10.8}'.format(s))
