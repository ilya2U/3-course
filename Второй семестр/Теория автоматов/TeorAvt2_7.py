

def proverka(P,T,N):
    cout = 0
    for key,value in P.items():
        if len(key)==1 and (key in N):
            cout+=1
        else:
            break
    return True if cout == len(P) else False


# A->wB or A->Bw or A->w         A,B - N         w - T*                праволинейная / леволинейная    Регулярный
def class3(Rules,NonTerminals, Terminals):
    temp = 0
    lev = False
    prav = False
    l = 0
    r = 0
    index = -1
    for left in Rules.keys():
        if len(left) == 1 and left in NonTerminals:
            for right in Rules[left]:
                nonterminalcount = 0
                for char in right:
                    if char in NonTerminals:
                        nonterminalcount += 1
                        index = right.find(char)
                if (nonterminalcount > 1):
                    break
                else:
                    if len(right) == 1 and nonterminalcount == 0:
                        r += 1
                        l += 1
                    else:
                        try:
                            if right[index - 1] in Terminals and right[index + 1] in Terminals:
                                break
                        except:
                            temp = 1

                        if str(right[0]) not in NonTerminals:
                            r += 1
                        else:
                            l += 1
        else:
            break
    k = 0
    for left in Rules.keys():
        for right in Rules[left]:
            k += 1
    if (l == k):
        lev = True
    elif (r == k):
        prav = True
    return lev, prav



# A->B                            A - N       B - (T or N)*       допускает E           Контекстно свободная
def class2(Rules,NonTerminals):
    k = 0
    for left in Rules.keys():
        for right in Rules[left]:
            k += 1
    KS = False
    counter = 0
    for left in Rules.keys():
        if (len(left) == 1 and left in NonTerminals):
            for right in Rules[left]:
                if len(right) > 0:
                    counter += 1
    if counter == k:
        KS = True
    else:
        KS = False
    return KS



# A -> B   len(A)<len(B)     не допускает S в B, допускает E            неукорачиваемая
# alpha -> beta         alpha = ksi A ksi     beta = ksi B ksi    A - N      B - (T or N)*     ksi - (T or N)*       Контекстно зависимая
def class1(Rules,NonTerminals ):
    k = 0
    for left in Rules.keys():
        for right in Rules[left]:
            k += 1
    neyk = False
    KZ = False
    counter = 0
    for left in Rules.keys():
        for right in Rules[left]:
            lind = 0
            lrind = len(left) - 1
            rrind = len(right) - 1
            leftl = ""
            rightl = ""
            leftr = ""
            rightr = ""
            try:
                while (left[lind] == right[lind]):
                    leftl += left[lind]
                    rightl += right[lind]
                    lind += 1
            except:
                break
            if (leftl != rightl):
                break
            while left[lrind] == right[rrind]:
                leftr += left[lrind]
                rightr += right[rrind]
                lrind -= 1
                rrind -= 1
            if leftr != rightr:
                break
            newL = ""
            newR = ""
            for i in range(lind, lrind + 1):
                newL += left[i]
            if (len(newL) != 1 or newL not in NonTerminals):
                break
            for i in range(lind, rrind + 1):
                newR += right[i]
            if len(newR) == 0 or newR == " ":
                break
            counter += 1
    if counter == k:
        KZ = True
    else:
        KZ = False
    counter = 0
    check = True
    if 'S' in Rules.keys() and " " in Rules['S']:
        for left in Rules.keys():
            for right in Rules[left]:
                for char in right:
                    if char == 'S': check = False
    if (check == True):
        for left in Rules.keys():
            for right in Rules[left]:
                if len(left) <= len(right): counter += 1
    if counter == k:
        neyk = True
    else:
        neyk = False
    return KZ, neyk



print('---------------------------------------------')
T = input('Введите терминалы через пробел (маленькие буквы) : ').split(' ')
N = input('Введите нетерминалы через пробел (большие буквы) : ').split(' ')
n = int(input('Введите количество правил: '))
P = {}
N.append('S')
for key in range(n):
    zap = input('Введите левую часть: ')
    P[zap] = input('Введите правую часть : ').split('|')
print('---------------------------------------------')
for keys,value in P.items():
    print('{} -> {}'.format(keys,value))
print('---------------------------------------------')
p = proverka(P,T,N)
if p == True:
    c3 = class3(P, N, T)
    c2 = class2(P, N)
    if c3[1] == True:
            print('Грамматика праволиейная, 3-го типа')
    elif c3[0] == True:
            print('Грамматика леволинейна, 3-го типа')
    elif c2 == True:
        print('Грамматика 2-го типа, контекстно-свободная')
else:
    c1 = class1(P, N)
    if c1[0] == True:
        print('Грамматика 1-го типа, контекстно-зависимая')
    elif c1[1] == True:
        print('Грамматика 1-го типа, неукорачиваемая')
    else:
        print('Грамматика 0-го типа')