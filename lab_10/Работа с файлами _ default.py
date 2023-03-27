#Программа для работы с записями в файлах
#Леонов Владислав ИУ7-16Б

import os
    
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
            tmp = open(file_name,'r')
            tmp.close()
            exception = False
        except BaseException:
            file_name = input('Имя файла некорректно. Введите имя файла: ')
    global is_file_opened, f, f_n
    if is_file_opened:
        f.close()
    f = open (file_name, 'r', encoding = 'UTF-8')
    if check_file(f,file_name):
        is_file_opened = True
        f_n = file_name
    else:
        f.close()
        print('Некорректное содержимое файла')
        return 0

#Проверка корректного формата файла
def check_file(f,file_name):
    if os.stat(file_name).st_size == 0:
        return False
    for line in f:
        if len(line.split('\t'))!=3:
            return False
    print('Файл успешно выбран.')
    return True

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
                    tmp1 = open(name_file,'w')
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
        f = open(name_file, 'w')
    else:
        f = open(name_file, 'w')
    t_ns = input('Введите названия трех полей через Tab:\n')
    while len(t_ns.split('\t')) != 3:
        t_ns = input('Вы ввели неверные названия полей, повторите ввод: ')
    t_ns = t_ns.split('\t')
    f.write('\t'.join([str(x) for x in t_ns])+'\n')
    r_c = input('Введите количество записей: ')
    while not r_c.isdigit():
        r_c = input('Вы ввели не число, повторите попытку: ')
    r_c = int(r_c)
    for i in range(r_c):
        f_t = input('Введите значение поля ' + t_ns[0]+ ': ')
        s_t = input('Введите значение поля ' + t_ns[1]+ ': ')
        t_t = input('Введите значение поля ' + t_ns[2]+ ': ')
        rec = '\t'.join((f_t, s_t, t_t))+'\n'
        f.write(rec)
        print()
    f.close()

#Вывод всех записей
def print_all_records():
    global f,is_file_opened,f_n
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        try:
            tmp = open(f_n,'r')
            tmp.close()
        except BaseException:
            print('Файла не существует.')
        print('Записи в файле:')
        f.seek(0)
        for line in f:
            tmp = line.split('\t')
            print('{:<30}{:<30}{:<20}'.format(tmp[0],tmp[1],tmp[2].strip()))
        f.close()
        f = open(f_n,'r', encoding = 'UTF-8')

#Поиск по 1 полю
def parametr_search():
    global f,is_file_opened,f_n
    if is_file_opened:
        try:
            tmp = open(f_n,'r')
            tmp.close()
            f.seek(0)
            k = 0
            for line in f:
                if k ==0:
                    pog = line.split('\t')
                    print('Поля:\n1)'+pog[0]+'\n2)'+pog[1]+'\n3)'+pog[2])
                    pole = input('Введите номер поля (1,2,3), которому будет \
производиться поиск: ')
                    while pole not in ('1', '2', '3'):
                        pole = input('Указанного поля не существует. Повторите ввод: ')
                    pole = int(pole)
                    key_word = input('\nВведите ключевое слово для поиска: ')
                    print('\nРезультат поиска:\n')
                    k = 1
                else:
                    tmp1 = line.split('\t')
                    if  (tmp1[pole-1].upper()).find(key_word.upper())!=-1:
                        print('{:<30}{:<30}{:<20}'.format(tmp1[0],tmp1[1],tmp1[2].strip()))
                        k = 2
            if k == 1:
                print('Нет записей, содержащих указанное ключевое слово в заданном поле')
            f.close() 
            f=open(f_n,'r', encoding = 'UTF-8')
        except BaseException:
            print('Файла не существует')
    else:
        print('Файл не открыт')
        

#Поиск по 2 полям
def double_parametr_search():
    global f,is_file_opened,f_n
    if is_file_opened:
        try:
            tmp = open(f_n,'r')
            tmp.close()
            f.seek(0)
            k = 0
            for line in f:
                if k == 0:
                    pog = line.split('\t')
                    print('Поля:\n1)'+pog[0]+'\n2)'+pog[1]+'\n3)'+pog[2])
                    pole1 = input('Введите первый номер поля, по которому будет \
производиться поиск: ')
                    while pole1 not in ('1', '2', '3'):
                        pole1 = input('Указанного поля не существует. Повторите ввод: ')
                    pole1 = int(pole1)
                    pole2 = input ('Введите второй номер поля, по которому будет \
производиться поиск: ')
                    while pole2 not in ('1', '2', '3') or pole2 == str(pole1):
                        pole2 = input('Некорректный ввод. Введите второе поле повторно: ')
                    pole2 = int(pole2)
                    key_word1 = input('\nВведите ключевое слово для поиска в первом поле: ')
                    key_word2 = input('Введите ключевое слово для поиска во втором поле: ')
                    print('\nРезультат поиска:\n')
                    k = 1
                else:
                    tmp1 = line.split('\t')
                    if  (tmp1[pole1-1].upper()).find(key_word1.upper())!=-1 and \
                    (tmp1[pole2-1].upper()).find(key_word2.upper())!=-1:
                        print('{:<30}{:<30}{:<20}'.format(tmp1[0],tmp1[1],tmp1[2].strip()))
                        k = 2
            if k == 1:
                print('Нет записей, содержащих указанное ключевое слово в заданном поле')
            f.close()
            f=open(f_n,'r', encoding = 'UTF-8')
        except BaseException:
            print('Файл не существует')
    else:
        print('Файл не открыт')

#Добавление записи
def add_new_record():
    global f,is_file_opened,f_n
    if not is_file_opened:
        print('Файл не открыт.')
    else:
        try:
            tmp = open(f_n,'a')
            tmp.close()
            f.close()
            f = open(f_n, 'r')
            titles = (f.readline()).split('\t')
            f.close()
            f=open(f_n,'a', encoding = 'UTF-8')
            pole1 = input('Введите значение поля '+ titles[0]+': ')
            pole2 = input('Введите значение поля '+ titles[1]+': ')
            pole3 = input('Введите значение поля '+ titles[2].strip()+': ')
            string = '\n'+pole1+'\t'+pole2+'\t'+pole3
            f.write(string)
            f.close()
            f = open(f_n, 'r',encoding = 'UTF-8')
        except BaseException:
            print('Файла не существует.')
                
#Проверка исходных данных
def check_choice(x):
    try: x = int(x)
    except ValueError: return False
    if x>6 or x<0: return False
    return True    

choice = 0
is_file_opened = False
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
