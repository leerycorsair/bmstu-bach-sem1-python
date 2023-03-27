
def sen_del(x):
    sogl_s = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ъ','ь']
    sogl_b = ['Б','В','Г','Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ь']
    b = ' '.join(x)
    b = b.split('.')
    for i in range(len(b)):
        m = mx = 0
        maxi_i = -1
        tmp = b[i]
        a = tmp.split(' ')
        for j in range(len(a)):
            for k in range(len(a[j])):
                if (a [j][k] in sogl_s) or (a [j][k] in sogl_b): m=1
            mx+=m 
            m = 0
        maxi = 0
        if maxi<mx:
            maxi_i= i
    print('Предложение с наибольшим количеством слов с согласными:')
    print (b[maxi_i])
    del(b[maxi_i])
    print()
    print('Текст без предложения выше: ')
    for i in range(len(b)):
        print(b[i]+'.')

text=[]
f = open('text.txt')
for line in f:
    text.append(line)
f.close()


for i in range (len(text)):
    print(text[i], end ='')
print()
sen_del(text)
    
  
