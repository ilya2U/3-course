import pandas as pd

#Ввод алфавита
rus = {"а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","0","1","2","3","4","5","6","7","8","9"}
eng = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"0","1","2","3","4","5","6","7","8","9"}

alphIsCorrect = False
while alphIsCorrect == False:
    print('Введите алфавит через пробел')
    print('(не должен содержать двойных и одинаковых символов, а так же символы должны быть из одного алфавита):')
    x = input()
    alph = x.split(' ')
    if set(alph[0]).issubset(rus):
        lang = rus
    else:
        lang = eng
    for i in alph:
        if (len(i) == 1) and (set(i).issubset(lang)) and (alph.count(i) == 1):
            alphIsCorrect = True
        else:
            alphIsCorrect = False
            break
#Ввод состоянй
statIsCorrect = False
while (statIsCorrect == False):
    print('Введите состояния автомата через пробел:')
    x = input()
    stats = x.split(' ')
    if (len(stats) >= 2):
        print(stats)
        statIsCorrect = True
#Проверка цепочек
while True:
    current = pStartStat
    wordIsCorrect = False
    again = True
    while (wordIsCorrect == False):
        print('Введите цепочку:')
        chain = input()
        for i in chain:
            for j in alph:
                if (i == j):
                    wordIsCorrect = True
                if wordIsCorrect == False:
                    break
chainList = list(chain)
while len(chainList) > 0:
        if DetDF[current].loc[chainList[0]] == '0':
            print('Автомат не пропускает эту цепочку')
            again = False
            break
        else:
            bef = current
            current = DetDF[current].loc[chainList[0]]
            chainList.pop(0)

        if (again == True) :
            if set([current]) <= set(pEndStats):
                print('Автомат пропускает эту цепочку')
            else:
                print('Автомат не пропускает эту цепочку')
        print()
