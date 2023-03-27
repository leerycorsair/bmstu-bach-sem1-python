#Программа для работы с записями в файлах
#Леонов Владислав ИУ7-16Б

import os
import pickle
    
#Выбор файла
def choose_file():
    print_c = False
    file_names = os.listdir()
    check = False
    for name in file_names:
        if name.find('.txt')!= -1:
            if print_c == False:
                print('Список файлов в директории:')
                print_c = True 
            print(name)
            check = True
    if check == False:
        print('В данной директории отсутствуют файлы.\n')
        cb_menu = input('Вернуться в меню (Да, Нет)?: ')
        while cb_menu.upper() not in ('ДА', 'НЕТ'):
            cb_menu = input('Некорректный ввод.Вернуться в меню (Да, Нет)?: ')
        if cb_menu.upper() == 'ДА': return 0
    file_name = input('Введите имя файла: ')
    exception = True
    while exception:
        try:
            tmp = open(file_name,'rb')
            tmp.close()
            exception = False
        except BaseException:
            file_name = input('Имя файла некорректно. Введите имя файла: ')
    global is_file_opened, f, f_n
    if is_file_opened:
        f.close()
    f = open(file_name, 'rb')
    o=True
    q=True
    k=0
    while q:
        try:
            y=pickle.load(f)
            if type(y)!=dict:
                o=False
                print('Некорректное содержимое файла.')
                q=False
            elif len(y)!=3:
                o=False
                print('Некорректное содержимое файла.')
                q=False
            elif k==0:
                global field
                field=y
                k=1
        except BaseException:
            q=False
    if k==0:
        o=False
        print('Некоректное содержимое файла.')
    if o:
        f.close()
        f=open(file_name,'rb')
        f_n = file_name
        is_file_opened = True
        print('Файл успешно выбран')
    else:
        f.close()


#Создание файла
def create_file():
    name_file = input('Введите имя файла: ')
    file_names = os.listdir()
    tmp = True
    while tmp:
        exception = True
        while exception:
            try:
                if name_file not in file_names:
                    tmp1 = open(name_file,'wb')
                exception = False
            except BaseException:
                name_file = input('Некорректное имя файла. Повторите ввод: ')
        if name_file in file_names:
            check = input('Файл с таким именем уже существует.\n\
Вы хотите его перезаписать(Да, Нет)? Ваш ответ: ')
            while check.upper() not in ('ДА', 'НЕТ'):
                check = input('Ввод некорректен. Повторите попытку(Да, Нет): ')
            if check.upper() == 'ДА':
                tmp = False
            else:
                name_file = input('Введите имя файла: ')
        else:
            tmp = False
    global is_file_opened, f
    if is_file_opened:
        is_file_opened = False
        f.close()
        f = open(name_file, 'wb')
    else:
        f = open(name_file, 'wb')
    a = {}
    for i in range(1,4):
        x=input('Введите название поля номер '+str(i)+': ')
        while len(x.split())!=1:
            x=input('Ввод некорректен. Введите название поля номер '+str(i)+': ')
        if i==1:
            a['Поле 1']=x
        elif i==2:
            a['Поле 2']=x
        else:
            a['Поле 3']=x
    pickle.dump(a,f)        
    r_c = input('Введите количество записей: ')
    while not r_c.isdigit():
        r_c = input('Вы ввели не число, повторите попытку: ')
    r_c = int(r_c)
    for i in range(1,r_c+1):
        x=input('Введите запись номер '+str(i)+'(Формат "поле1 поле2 поле3"): ')
        while len(x.split())!=3:
            x=input('Запись введена неккоректно. Повторите ввод(Формат "поле1 поле2 поле3"): ')
        while x.find(' ')!=-1:
            x=x.replace(' ','\t')
        x=x.split('\t')
        b={}
        b[a['Поле 1']]=x[0]
        b[a['Поле 2']]=x[1]
        b[a['Поле 3']]=x[2]
        if i!=r_c:
            pickle.dump(b,f)
        else:
            pickle.dump(b,f)
    f.close()

#Вывод всех записей
def print_all_records():
    global f,is_file_opened,f_n
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        try:
            tmp = open(f_n,'rb')
            tmp.close()
        except BaseException:
            print('Файла не существует.')
        print('Записи в файле:')
        check = 0
        q = True
        while q:
            try:
                y=pickle.load(f)
                if check == 0:
                    print('Поля: '+'{:^30}'.format(y['Поле 1'])+' '+'{:^30}'.format(y['Поле 2'])\
                          +' '+'{:^30}'.format(y['Поле 3'])+'\n')
                    check = 1
                    a=y
                else:
                    print('      '+'{:^30}'.format(y[a['Поле 1']])+' '+'{:^30}'.format(y[a['Поле 2']])\
                          +' '+'{:^30}'.format(y[a['Поле 3']]))
            except BaseException:
                q = False
        f.close()
        f = open(f_n,'rb')

#Поиск по 1 полю
def parametr_search():
    global f,is_file_opened,f_n,field
    exception=False
    try:
        u=open(f_n,'rb')
        u.close()
        exception = True
    except BaseException:
        print('Файла не существует.')
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        print('Поля файла: ')
        for i in range(1,4):
            print(str(i)+') '+field['Поле '+str(i)])
        x=input('Введите номер поля, по которому будет производиться поиск: ')
        while not x in {'1','2','3'}:
            x=input('Номер поля введен некорректно. Повторите ввод: ')
        x=int(x)
        key_word=input('Введите значение поля для поиска: ')
        print('\nЗаписи, удовлетворяющие критерию поиска: \n')
        print('Поля: '+'{:^30}'.format(field['Поле 1'])+' '+'{:^30}'.format(field['Поле 2'])+' '+'{:^30}'.format(field['Поле 3'])+'\n')
        k=0
        q=True
        y=pickle.load(f)
        while q:
            try:
                y = pickle.load(f)
                if y[field['Поле '+str(x)]] == key_word:
                    print('      '+'{:^30}'.format(y[field['Поле 1']])+' '+'{:^30}'.format(y[field['Поле 2']])+' '+'{:^30}'.format(y[field['Поле 3']]))
                    k+=1
            except BaseException:
                q=False
        if k == 0:
            print('Нет записей, удовлетворяющих условию.')
        f.close() 
        f=open(f_n,'rb')

#Поиск по 2 полям
def double_parametr_search():
    global f,is_file_opened,f_n,field
    exception=False
    try:
        u=open(f_n,'rb')
        u.close()
        exception = True
    except BaseException:
        print('Файла не существует.')
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        print('Поля файла: ')
        for i in range(1,4):
            print(str(i)+') '+field['Поле '+str(i)])
        x=input('Введите номер первого поля, по которому будет производиться поиск: ')
        while not x in {'1','2','3'}:
            x=input('Номер поля введен некорректно. Повторите ввод: ')
        x=int(x)
        key_word1=input('Введите значение поля для поиска: ')
        z=input('Введите номер второго поля, по которому будет производиться поиск: ')
        while not z in {'1','2','3'}:
            z=input('Номер поля введен некорректно. Повторите ввод: ')
        z=int(z)
        criterion2=input('Введите значение поля для поиска: ')
        print('Записи, удовлетворяющие критерию поиска: \n')
        print('Поля: '+'{:^30}'.format(field['Поле 1'])+' '+'{:^30}'.format(field['Поле 2'])+' '+'{:^30}'.format(field['Поле 3'])+'\n')
        k=0
        q=True
        y=pickle.load(f)
        while q:
            try:
                y=pickle.load(f)
                if y[field['Поле '+str(x)]] == key_word1 and y[field['Поле '+str(z)]] == key_word2:
                    print('      '+'{:^30}'.format(y[field['Поле 1']])+' '+'{:^30}'.format(y[field['Поле 2']])+' '+'{:^30}'.format(y[field['Поле 3']]))
                    k+=1
            except BaseException:
                q=False
        if k==0:
            print('Нет записей, удовлетворяющих условию.')
        f.close() 
        f=open(f_n,'rb')
#Добавление записи
def add_new_record():
    global f,is_file_opened,f_n,field
    exception=False
    try:
        u=open(f_n,'rb')
        u.close()
        exception = True
    except BaseException:
        print('Файла не существует.')
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        f=open(f_n,'ab')
        x=input('Введите запись(Формат "поле1 поле2 поле3"): ')
        while len(x.split())!=3:
            x=input('Запись введена некорректно. Повторите ввод(Формат "поле1 поле2 поле3"): ')
        while x.find(' ')!=-1:
            x=x.replace(' ','\t')
        x=x.split('\t')
        b={}
        b[field['Поле 1']]=x[0]
        b[field['Поле 2']]=x[1]
        b[field['Поле 3']]=x[2]
        pickle.dump(b,f)
        f.close()
        f=open(f_n,'rb')
                
#Проверка исходных данных
def check_choice(x):
    try: x = int(x)
    except ValueError: return False
    if x>6 or x<0: return False
    return True    

choice = 0
is_file_opened = False
f_n = ''
while choice != 6:
    menu = 'Опции программы:\n\
0 - Выбрать файл\n\
1 - Создать файл\n\
2 - Вывести все записи\n\
3 - Поиск по 1 полю\n\
4 - Поиск по 2 полям\n\
5 - Добавить запись\n\
6 - Выход из программы'
    print (menu)
    choice = input('Выберите опцию: ')
    if check_choice(choice):
        choice = int(choice)
    else:
        while check_choice(choice) != True:
            print(menu)
            choice = input('Вы совершили ошибку при вводе, повторите попытку:')
    choice = int(choice)
    if choice == 0:
        print()
        choose_file()
        print()
    if choice == 1:
        print()
        create_file()
        print()
    if choice == 2:
        print()
        print_all_records()
        print()
    if choice == 3:
        print()
        parametr_search()
        print()
    if choice == 4:
        print()
        double_parametr_search()
        print()
    if choice == 5:
        print()
        add_new_record()
        print()
print('Программа успешно завершена.')
