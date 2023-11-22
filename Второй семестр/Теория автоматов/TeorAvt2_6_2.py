alph = (input('Введите алфавит через пробел: ')).split(' ')
n1 = int(input('Введите количество начальных состояний: '))
n2 = int(input('Введите количество конечных состояний: '))
n = n1+n2
nach = []
kon = []
for i in range(n1):
    nach.append(input('Введите начальное очередное состояния: '))
for i in range(n2):
    kon.append(input('Введите конечное очередное состояния: '))
print('--------------------------------')
sost = {}
versh = []
perexod = set()
vspom = []
for i in range(n):
    if i<n1:
        for j in alph:
            vspom.append(input('Введите, куда можно попасть из {} по {} '.format(nach[i],j)))
        versh.append(nach[i])
        perexod.add(vspom[0])
        perexod.add(vspom[1])
        sost[nach[i]] = vspom
        vspom = []
    else:
        for j in alph:
            vspom.append(input('Введите, куда можно попасть из {} по {} '.format(kon[i-n1], j)))
        versh.append(kon[i-n1])
        perexod.add(vspom[0])
        perexod.add(vspom[1])
        sost[kon[i-n1]] = vspom
        vspom = []
print('--------------------------------')
print(versh)
print(perexod)
print('--------------------------------')
print('1) Автомат детерменизирован')
dost = False
for k in range(2):
    for i in versh:
        if i != 'q0':
            if i not in perexod:
                sost.pop(i)
                print('Вершина {} не достижима'.format(i))
                if i in nach:
                    nach.remove(i)
                else:
                    kon.remove(i)
                versh.remove(i)
    perexod.add('q0')

    perexod = set()
    for key, value in sost.items():
        for j in value:
            if key == j:
                continue
            else:
                perexod.add(j)

if len(versh) == n:
    print('2) Все вершины достижимы')

for key, value in sost.items():
    print('{}, {} ---> {}'.format(key,alph[0], value[0]),' | ','{}, {} ---> {}'.format(key,alph[1], value[1]))

versh = []
perexod = []
for key, value in sost.items():
    versh.append(key)
    perexod.append(value)
print('--------------------------------')

print('0 эквивалентность ----- {},{}'.format(nach,kon))

out = []
prom_out = [nach,kon]
prov = []
prov2 = []
proooom = []
level = 1
prom_tochno_out = [nach,kon]
check = 0
check2 = 0
while out != prom_tochno_out:
    out = prom_tochno_out
    prom_out = prom_tochno_out
    prom_tochno_out = []
    proooom = []
    for i in range(len(prom_out)):
        check = 0
        check2 = 0
        prom_tochno_out.append([])
        if len(''.join(prom_out[i])) > 3:
            for j in range(len(prom_out[i])):
                if sost.get(prom_out[i][j])[0] not in prom_out[i] or sost.get(prom_out[i][j])[1] not in prom_out[i]:
                    prov.append(prom_out[i][j])
                    if len(prov) == 1 and j == len(prom_out[i])-1:
                        proooom.append(prov)
                        prov = []

                else:
                    prom_tochno_out[i].append(prom_out[i][j])
                    if len(prov) == 1 and j == len(prom_out[i])-1:
                        proooom.append(prov)
                        prov = []

        else:
            prom_tochno_out[i].append(prom_out[i][0])
        if len(prov)>1:
            for k in range(len(prom_out)):
                if (sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]) and (sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) and (sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) and (sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]):
                    proooom.append(prov)
                    prov = []
                    break
                elif (sost.get(prov[0])[0] == sost.get(prov[1])[0]) and (sost.get(prov[0])[1] == sost.get(prov[1])[1]) or (sost.get(prov[0])[0] == sost.get(prov[1])[1]) and (sost.get(prov[0])[1] == sost.get(prov[1])[0]):
                    proooom.append(prov)
                    prov = []
                    break
                elif ((sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]) and (sost.get(prov[0])[1] == sost.get(prov[1])[1])) or ((sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) and (sost.get(prov[0])[0] == sost.get(prov[1])[0])):
                    proooom.append(prov)
                    prov = []
                    break
                elif ((sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) and (sost.get(prov[0])[1] == sost.get(prov[1])[0])) or ((sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]) and (sost.get(prov[0])[0] == sost.get(prov[1])[1])):
                    proooom.append(prov)
                    prov = []
                    break
                elif ((prov[0] == sost.get(prov[1])[1] and prov[1] == sost.get(prov[0])[1] and sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]) or (prov[0] == sost.get(prov[1])[0] and prov[1] == sost.get(prov[0])[0] and sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) ) :
                    proooom.append(prov)
                    prov = []
                    break
                elif ((sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k]) or (sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) or (sost.get(prov[0])[0] in prom_out[k] and sost.get(prov[1])[1] in prom_out[k]) or (sost.get(prov[0])[1] in prom_out[k] and sost.get(prov[1])[0] in prom_out[k])) :
                    check2 += 1
                else:
                    check += 1
            if check == len(prom_out):
                proooom.append([prov[0]])
                proooom.append([prov[1]])
                prov = []
            elif check2 == len(prom_out):
                proooom.append(prov)
                prov = []
            elif len(prov)>0:
                proooom.append([prov[0]])
                proooom.append([prov[1]])
                prov = []
    for i in range(len(proooom)):
        prom_tochno_out.append(proooom[i])

    for i in range(len(prom_tochno_out)):
        if [] in prom_tochno_out:
            prom_tochno_out.remove([])
    prom_tochno_out.sort()
    print('{} эквивалентность -----'.format(level), '{}'.format(prom_tochno_out))
    level += 1
    if level > 10:
        break

new_sost = {}
vspom = []
print('--------------------------------')
new_sost_out = {}
vspom4 = []
vspom5 = []
for per in prom_tochno_out:
    if len(per)>1:
        for m in per:
            vspom.append(sost.get(m))
    else:
        vspom.append(sost.get(per[0]))
    if len(per) > 1:
        new_sost[','.join(per)] = vspom
        vspom = []
    else:
        new_sost[per[0]] = vspom[0]
        vspom = []

for key, value in new_sost.items():
    if len(key) > 3:
        vspom3 = key.split(',')
        key_new = vspom3[0]
        vspom3.pop(0)
        for m in vspom3:
            for value2 in new_sost.values():
                if len(value2[0][0]) > 1:
                    if m in value2[0]:
                        vspom5.append(value2[0])
                        vspom5[0][vspom5[0].index(m)] = key_new
                    else:
                        vspom5.append(value2[0])
                    vspom4.append(vspom5[0])
                    vspom5 = []
                else:
                    if m in value2:
                        vspom5.append(value2)
                        vspom5[0][vspom5[0].index(m)] = key_new
                        vspom4.append(vspom5[0])
                        vspom5 = []
                    else:
                        vspom4.append(value2)
            sost.pop(m)
ind = 0
for key in new_sost.keys():
    new_sost_out[key] = vspom4[ind]
    ind += 1

for key, value in sost.items():
    print('{}, {} ---> {}'.format(key,alph[0], value[0]),' | ','{}, {} ---> {}'.format(key,alph[1], value[1]))



