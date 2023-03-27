import math
a1=float(input('Начало: '))
a2=float(input('Конец: '))
a10=a1
step=float(input('Шаг: '))
eps=1e-5
eps1=1e-3
iter=int((a2-a1+eps)/step)
sr=60
y1max=math.cos(a1)-1
y1min=math.cos(a1)-1
for k in range(iter+1):
    y1=math.cos(a10)-1
    if y1>y1max:
        y1max=y1
    if y1<y1min:
        y1min=y1
    a10+=step
print(8*' ', '{:^8.3}'.format(y1min),(sr-8)*' ','{:^8.3}'.format(y1max),sep='')
print(13*' ','|', (sr-2)*'_','|',sep='')
while a1<a2:
    y1=math.cos(a1)-1
    space_function=int((y1-y1min+eps)/(y1max-y1min)*(sr-1))
    space_liney=int((0-y1min+eps)/(y1max-y1min)*(sr-1))
    if abs(y1max)<eps:
        if space_liney==space_function:
            print('{:^13.6}'.format(a1),space_function*' ','*',sep='')
        else:
            if abs(y1)<eps1:
                print('{:^13.6}'.format(a1),(space_function+1)*' ','*',sep='')
            else:
                print('{:^13.6}'.format(a1),space_function*' ','*',
                    (space_liney-space_function-1)*' ','|',sep='')
    else:
        print('{:^13.6}'.format(a1),space_function*' ','*',sep='')
    a1+=step
