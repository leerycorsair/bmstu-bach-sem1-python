#Функция для проверки корректности ввода базы кодов согласно формату
def check_base_line (line):
        if line.count(' ') == 1 and line.count('$') == 1:
            if line[:line.index(' ')].isdigit() \
            and line[line.index(' ')+1:line.index('$')].isalpha()\
            and line[line.index('$')+1:len(line)].isdigit(): return True
            else: return False
        else: return False

#Функция для проверки корректности ввода базы телефонных звонков согласно формату
def check_calls_line (line):
        if line.count(' ') >= 1 :
            if (line[:line.rindex(' ')].replace(' ','')).isdigit() \
            and line[line.rindex(' ')+1:len(line)].isdigit(): return True
            else: return False
        else: return False
        
print('*'*80,end = '\n\n')
print('Уважаемый  пользователь, Вас  приветствует программа для \n\
обработки данных о телефонном звонке и выводе информации \n\
о каждом звонке в формате отчета.', end = '\n\n\n')

#Ввод базы кодов телефонных звонков
print('Вводите  международные и междугородние  телефонные коды,\n\
пункт назначения и соответствующий тарифный план:')
p_base = []
while True:
    line = input()
    if line =='000000': break

    #Проверка корректности данных
    while not check_base_line(line):
        line = input('Вы ввели неформатную строку, повторите ввод:\n')

    line = line.replace('$',' ')
    line = line.split(' ')
    p_base.append(line)

#Ввод базы телефонных звонков
print('\nВводите номера звонков и их продолжительность:')
p_calls = []
while True:
    line = input()
    if line == '#': break

    #Проверка корректности данных
    while not check_calls_line(line):
        line = input('Вы ввели неформатную строку, повторите ввод:\n')

    line = list(line.rpartition(' '))
    line[0] = line[0].replace(' ','')
    del (line[1])
    p_calls.append(line)

for i in range(len(p_calls)):
    #Проверка: является ли данный номер местным
    if p_calls[i][0][0]!='0':
        #Печать местных звонков
        print('{:<16}{:<26}{:<15}{:<5}{:<5}{:<5}'.format(p_calls[i][0],\
                'Local', p_calls[i][0], p_calls[i][1],'0.00', '0.00'))
    else:
        found = False
        for j in range(len(p_base)):
            #Проверка: есть ли данный номер в базе телефонных кодов
            if p_calls[i][0].find(p_base[j][0]) == 0:
                found = True
                #Печать звонков, найденных в базе телефонных кодов
                print('{:<16}{:<26}{:<15}{:<5}{:<5}{:<5}'.format(p_calls[i][0],\
        p_base[j][1], p_calls[i][0].replace(p_base[j][0],''),\
        p_calls[i][1],int(p_base[j][2])/100, int(p_base[j][2]) * int(p_calls[i][1])/100))
                break
        #Печать звонков отсутвующих в базе телефонных кодов
        if found == False:
                print('{:<16}{:<26}{:<15}{:<5}{:<5}{:<5}'.format(p_calls[i][0],\
               'Unknown', '', p_calls[i][1],'', '-1.00'))

#Оповещение пользователя об успешном завершении программы
print('\nПрограмма успешно завершена.',end = '\n\n')
print('*'*80)
