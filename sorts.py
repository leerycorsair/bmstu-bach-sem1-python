from random import*
from datetime import datetime

print('Bubble sort')
a = [ randint(1,100) for i in range (10)]
print(a)
for i in range(len(a) - 1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
print(a, '\n'*3)

print('Bubble mod = Coctail sort')
a = [ randint(1,100) for i in range (10)]
print(a)
lf = 0; rg = len(a)-1
while lf<rg:
    for i in range(lf,rg,1):
        if a[i]> a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    rg = rg - 1
    if lf<rg:
        for i in range(rg,lf,-1):
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
        lf = lf + 1
print(a, '\n'*3)

print('Insertion sort')
a = [ randint(1,100) for i in range (10)]
print(a)
for i in range(1,len(a)):
    x = a[i]
    j = i
    while (j > 0 and a[j-1] > x):
        a[j]= a[j-1]
        j = j - 1
    a[j] = x
print(a, '\n'*3)

print('Selection sort')
a = [ randint(1,100) for i in range (10)]
print(a)
for i in range((len(a)-1)):
    m = i
    j = i+1
    while j < len(a):
        if a[j]<a[m]:
            m = j
        j += 1
    a[i],a[m]=a[m],a[i]
print(a, '\n'*3)




print('Shell sort')

def shellSort(array):
	increment = len(array) // 2
	while increment > 0:
		for startPosition in range(increment):
			gapInsertionSort(array, startPosition, increment)
		increment //= 2

def gapInsertionSort(array, low, gap):
	for i in range(low + gap, len(array), gap):
		currentvalue = array[i]
		position = i
		while position >= gap and array[position - gap] > currentvalue:
			array[position] = array[position - gap]
			position = position - gap
		array[position] = currentvalue
		
a = [ randint(1,100) for i in range (10)]
print(a)
shellSort(a)
print(a, '\n'*3)




print('Quick sort')

seed(100)
a = [randint(1,100) for i in range (9999)]

def quicksort(a, l, r):
    if l>=r:return
    x = a[(l+r)//2]
    i = l; j = r
    while i<j:
        while a[i]<x: i+=1
        while a[j]>x: j-=1
        if i<=j:
            a[i],a[j]=a[j],a[i]
            i+=1;j-=1
    quicksort(a,l,j)
    quicksort(a,i,r)
    
t1 = datetime.now()
quicksort(a,0,len(a)-1)
t2 = datetime.now()
print('Time = ', (t2 - t1).microseconds)

seed(100)
a = [randint(1,100) for i in range (9999)]
t1 = datetime.now()
a.sort()
t2 = datetime.now()
print('Time = ', (t2 - t1).microseconds)

