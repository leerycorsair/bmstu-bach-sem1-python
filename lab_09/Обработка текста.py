#Программа для обработки текста различными методами

#Леонов Владислав
#ИУ7-16Б

#проверка выбора действия
def check_input():
    while True:
        try:
            choice = int(input())
        except (ValueError, TypeError):
            print()
            print('Некорректные данные! Повторите ввод')
        else:
            if choice >= 1 and choice <= 8:
                break
            else:
                print()
                print('Некорректные данные! Повторите ввод!')
    return choice

#Выравнивание по левому краю
def left (x):
    for i in range(len(x)):
        b = x[i].lstrip()
        b = b.split()
        b = ' '.join(b)
        x[i] = b
    return(x)

#Выравнивание по правому краю
def right (x):
    x = left(x)
    max_str_len = 0
    for i in range (len(x)):
        if len(x[i]) > max_str_len: max_str_len = len(x[i])
    for i in range (len(x)):
        while len(x[i]) < max_str_len: x[i] = ' ' + x[i]
    return(x)

#Выравнивание по ширине одной строки
def line_width(line, ma):
    length = len(line)
    count = 0
    for i in range(length):
        if not line[i].isspace(): count = 1
    move = ' '
    if count == 1:
        while len(line) < ma:
            i = 0
            while i < len(line):
                if len(line) >= ma: break
                if line[i].isspace() and not line[i+1].isspace():
                    line = line[:i] + move + line[i:]
                    i += len(move)
                i+=1
    return line

#Выравнивание по ширине всего текста
def width(arr):
    max_str_len = 0
    for i in range (len(arr)):
        if len(arr[i]) > max_str_len: max_str_len = len(arr[i])
    left(arr)
    for i in range(len(arr)):
        arr[i] = line_width(arr[i],max_str_len)
    return arr

#Глобальное выравнивание
def global_eq(x,m):
    if m == 1: left (x)
    if m == 2: right(x)
    if m == 3: width(x)
    return (x)

#Замена слова
def word_replace(x,word_for_change,word_to_change,m):
    for i in range(len(x)):
        b = x[i]
        b = b.replace(word_for_change,word_to_change)
        word_for_change = word_for_change. capitalize()
        b = b.replace(word_for_change,word_to_change)
        x[i] = b
    global_eq(x,m)
    return x

#Удаление слова
def word_delete(x,word_for_delete,m):
    word_replace(x,word_for_delete,'',m)
    return(x)
        
#Замена сложения и вычитания в строке на их результат

def line_calculate(line):
    i = 0
    j = 0
    op_1 = op_2 = res = sign = ''
    while i < len(line):
        if line[i].isdigit():
            if i>0:
                if line[i-1]=='+' or line[i-1]=='-':
                    op_1 = line[i-1] +op_1
                    j = i-1
                else: j = i
            while line[i].isdigit():
                op_1 = op_1 + line[i]
                i+=1
            if ((line[i]=='+' or line[i]=='-' ) and line[i+1].isdigit()) or (line[i+1]==line[i]=='-'and line[i+2].isdigit()):
                sign = line[i]
                i+=1
                while line[i].isdigit():
                    op_2 = op_2 + line[i]
                    i+=1
                length = len(op_1 + sign + op_2)
                check = False
                if j>0 and not line[j-1].isalpha() and not line[j+length].isalpha():
                    check = True
                if j==0 and not line[j+length].isalpha():
                    check = True
                if check==True:                        
                    if sign == '+':
                        res = int(int(op_1)+int(op_2))
                    if sign == '-':
                        res = int(op_1)-int(op_2)
                    line = line[:j] + str(res) + line[(j+length):]
                
            op_1 = op_2 = res = sign = ''
            j = length = 0
        else:
            i+=1
    return line


#арифметические операции в тексте
def text_calculate(arr):
    for i in range(len(arr)):
        arr[i] = line_calculate(arr[i])
    return arr

#Поиск предложения с минимальным количеством слов,
#в которых гласные чередуются с согласными
def sen_search(x):
    glas = ['а','е','ё', 'и', 'о', 'у', 'э','ы','ю','я']
    sogl = ['б','в','г','д','ж','з','й','к','л','м','н','п','р','с','т','ф','х','ц','ч','ш','щ','ъ','ь']      
    tmp = ' '.join(x)
    tmp = tmp.replace('!','.')
    tmp = tmp.replace('?','.')
    tmp = tmp.replace(',','')
    tmp_f = tmp.split('.')
    tmp = tmp.replace('"','')
    tmp = tmp.lower()
    i_sen = -1
    num_of_words = 0
    min_w = 1000
    m = 1
    tmp = tmp.split('.')
    for i in range(len(tmp)):
        b = tmp[i].split()
        for j in range(len(b)):
            for k in range(len(b[j]) - 1):
                if not ((b[j][k] in glas and b[j][k+1] in sogl) or (b[j][k] in sogl and b[j][k+1] in glas)): m = 0
            num_of_words += m
            m = 1
        if num_of_words < min_w:
            min_w = num_of_words
            i_sen = i
        num_of_words = 0
    return(tmp_f[i_sen]+'.')
        

#Считывание текста из файла
text=[]
f = open('text.txt')
for line in f:
    text.append(line[:len(line)-1])
f.close()
m=0
for i in range (len(text)):
    print(text[i])

choice = 0
while True:
    #вывод меню
    file_2 = open('menu.txt')
    menu = file_2.read()
    print(menu)
    file_2.close()

    #выбор действия
    print('Выбери действие: ', end =' ')
    choice = check_input() 
    print()

    #преобразования текста согласно выбранному действию
    if choice == 1:
        text = width(text)
        m = 3
    if choice == 2:
        text = left(text)
        m = 1
    if choice == 3:
        m = 2
        text = right(text)
    if choice == 4:
        word_1 = input('Введите слово, которое нужно заменить: ')                    
        word_2 = input('Введите слово, на которое нужно заменить: ')
        text = word_replace(text, word_1, word_2,m)
    if choice == 5:
        word = input(('Введите слово, которое нужно удалить: '))
        text = word_delete(text,word,m)
    if choice == 6:
        text_calculate(text)
    if choice == 7:
        a = sen_search(text)
        a = a.split()
        a = ' '.join(a)
        print(a)
    if choice == 8:
        print('Программа закончена!')
        break
    if choice != 7:
        print()
        for i in range (len(text)):
            print(text[i])

