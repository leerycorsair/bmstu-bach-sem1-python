#Защита

import pickle

f1 = open('f1.txt','r')
f2 = open('f2.txt','rb')

a = f1.readline()
a = float(a)
b = pickle.load(f2)
b = float(b)

f1.close()
f2.close()

summa = a + b
proizvedenie = a * b

f3 = open('f3.txt', 'w')
f4 = open('f4.txt', 'wb')


f3.write('Сумма = '+ str('{:10}'.format(summa)))
pickle.dump( 'Произведение = '+ str('{:10}'.format(proizvedenie)),f4)
f3.close()
f4.close()
