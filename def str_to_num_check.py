
def str_to_num_check(x):
    dot_check = 0
    e_check = 0
    plus_minus_check = 0
    if x =='': return False
    x = ' ' + x
    for i in range(1,len(x)):
        if (x[i]>'9' or x[i]<'0') and x[i]!='+' and x[i]!='-' and x[i]!='e'and x[i]!='.' and x[i]!='E': return False
        if x[i]=='.':
            dot_check += 1
        if x[i]=='+' or x[i]=='-':
            plus_minus_check += 1
        if x[i]=='e' or x[i]=='E':
            e_check += 1
        if dot_check > 1 or e_check > 1: return False
        if plus_minus_check > 1 and e_check == 0: return False
        if x[i] == '.' and e_check == 1: return False
        if (x[i] == '+' or x[i] == '-') and dot_check == 1 and e_check == 0: return False
        if (x[i] == '+' or x[i] == '-') and ('0'<=x[i-1]<='9' or x[i-1]=='.'): return False
    if (x[1] == '+' or x[1] == '-') and (x[2] == 'e' or x[2] == 'E'): return False
    if x[1] == 'e' or x[1] == 'E': return False
    if x == '.': return False
    if x[len(x)-1] == 'e' or x[len(x)-1] == 'E' or x[len(x)-1] == '-' or x[len(x)-1] == '+' :return False
    return True

'''
def str_to_num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        print('Вы ввели число с ошибкой')
        return False
'''
x=input()
print(str_to_num_check(x))


