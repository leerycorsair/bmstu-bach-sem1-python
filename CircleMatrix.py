def filler():
    global a, num,i,j
    k = 0
    while a[i][j+1]== 0:
        a[i][j+1] = num
        num += 1
        j += 1
        k += 1
    while a[i+1][j] == 0:
        a[i+1][j] = num
        num += 1
        i += 1
        k += 1
    while a[i-1][j-1] == 0:
        a[i-1][j-1] = num
        num += 1
        i -= 1
        j -= 1
        k += 1
    if k>0: filler()

x = int(input())

a = [[0]*x for i in range (x)]
i=0
j=0
num = 1
while j < x - 1:
    a[0][j] = num
    j += 1
    num += 1
while i<x-1:
    a[i][x-1] = num
    i+=1
    num += 1   
while a[i][j] == 0:
    a[i][j] = num
    num += 1
    i -= 1
    j -= 1
i += 1
j += 1
filler()
for k in a:
    for m in k:
        print('{:4}'.format(m), end = '')
    print()    
