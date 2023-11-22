rus = set('абвгдежзийклмнопрстуфхцчшщъыьэюя')
eng = set('abcdefghijklmnopqrstuvwxyz')
nom = set('1234567890')
while True:
    ran = input('''1 алфавит;\n2 число в слово;\n3 слово в число;\n4 выход: ''')
    if ran == '1':
        alt = {}
        i = 1
        while True:
            sim = input('Введите {} - й символ алфавита или пробел: '.format(i))
            if sim == ' ':
                break
            if sim in alt.values():
                print('\n{} уже есть, введите другую букву.\n'.format(sim))
                continue
            alt[i] = sim
            i += 1
        for j in alt:
            if j in rus:
                print('\n''Алфавит: {}\n'.format(list(alt.values())))
            if j in eng:
                print('\n''Алфавит: {}\n'.format(list(alt.values())))
            if j in nom:
                print('\n''Алфавит: {}\n'.format(list(alt.values())))
        print('\nВведите алфавит заново!!\n')
    elif ran == '2':
        num = int(input('Введите число: '))
        try:
            a = []
            n = len(alt)
            i = 0
            while num // n != 0:
                if num % n == 0:
                    a.append(n)
                    num = (num // n) - 1
                else:
                    a.append(num % n)
                    num = num // n
                i += 1
                print(num)
            print(list(reversed(a)))
            if num != 0:
                a.append(num)
            a = a[::-1]
            slv = []
            for i in range(len(a)):
                slv.append(alt[a[i]])
            slv = ' '.join(slv)
            print(slv)
        except:
            print('\nНеобходимо задать алфавит!\n')
    elif ran == '3':
        try:
            word = input('Введите слово: ')
            temp = []
            for i in word:
                if i not in alt.values():
                    print('\nСлово не принадлежит алфавиту!\n')
            for i in range(len(word)):
                temp.append(word[i])
            total = 0
            power = len(temp) - 1
            for i in range(len(temp)):
                for key in alt.keys():
                    if alt[key] == temp[i]:
                        total = total + key * (len(alt) ** power)
                        power = power - 1
                        print('({}^{})*{}'.format(len(alt), power+1, key))
            print(total)
        except:
            print('\nНеобходимо задать алфавит!\n')
    elif ran == '4':
        break
    else:
        print('\nНеобходимо ввести 1, 2, 3 или 4.')
