import pandas as pd

n = input("Введите алфавит: ")
alphavet = n.split()
print(alphavet)
m = int(input("Введите количество вершин: "))
vershini = ["q" + str(i) for i in range(m)]
start = input("Введите начальную вершину: ")
end = input("Введите конечную вершину: ").split()

slovar = {}
for i in vershini:
    slovar2 = {}
    for j in alphavet:
        print("Куда можно пройти из ", i, " по ", j, "?")
        n = input().split()
        slovar2[j] = set(n)
    print("Куда можно пройти из ", i, " по E ?")
    f = input().split()
    f.append(i)
    slovar2["E"] = set(f)
    slovar[i] = slovar2

for i in slovar:
    # Объединяем значения вершин, соединенные eps
    tmp = []
    tmp = slovar[i]["E"]
    for j in tmp.copy():
        for k in alphavet:
            slovar[i][k] |= slovar[j][k]
            slovar[i]["E"] |= slovar[j]["E"]
    tmp = []
    for f in range(3):
        for k in alphavet:
            tmp = slovar[i][k]
            for j in tmp.copy():
                slovar[i][k] |= slovar[j]["E"]
print("\n", slovar)

# Создаем S-ки
slist = {}
k = 0
for i in vershini:
    slist["S" + str(k)] = slovar[i]["E"]
    k += 1
print("\n", slist, "\n")

endTmp = []
count2 = len(slist) - len(end)
if len(end) > 1:
    for i in end:
        count2 += 1
        count = 0
        for j in slist:
            for k in slist[j]:
                if i in k:
                    endTmp.append(j)
                    count += 1
            if count == count2:
                break

else:
    for i in slist:
        for j in slist[i]:
            if end[0] in j:
                endTmp.append(i)
endTmp = list(set(endTmp))
print(endTmp)

# Создаем словарь с S
s2list = {}
for i in slist:
    tmpslov = {}
    for k in alphavet:
        tmp2 = []
        n = set()
        for j in list(slist[i]):
            n = n.union(slovar[j][k])
        for j in slist:
            if (slist[j] <= n):
                tmp2.append(j)
        tmpslov[k] = set(tmp2)
    s2list[i] = tmpslov
df = pd.DataFrame(s2list)
df = df.T
print(df, "\n")

# Создаем P
pslovar = {}
tmp = []
tmp2 = []
for i in slist:
    if (slist[i] <= slovar[start]["E"]):
        tmp2.append(i)
tmp.append(set(tmp2))
pslovar["P0"] = set(tmp2)
p2slovar = ["P0"]
f = 1
w = 0
plist = {}
while w < len(pslovar):
    tmpslov = {}
    for k in alphavet:
        n = set()
        for j in pslovar[p2slovar[w]]:
            n = n.union(s2list[j][k])
        if n in tmp:
            for j in pslovar:
                if pslovar[j] == n:
                    tmpslov[k] = j
        elif n == set():
            tmpslov[k] = set()
        else:
            tmp.append(n)
            pslovar["P" + str(f)] = n
            tmpslov[k] = "P" + str(f)
            p2slovar.append("P" + str(f))
            f += 1
    plist["P" + str(w)] = tmpslov
    w += 1
print(pslovar, "\n")
df1 = pd.DataFrame(plist)
df1 = df1.T
print(df1)

# PROVERKA
pEnd = []
count2 = len(pslovar) - len(endTmp)
if len(endTmp) > 1:
    for i in endTmp:
        count2 += 1
        count = 0
        for j in pslovar:
            for k in pslovar[j]:
                if i in k:
                    pEnd.append(j)
                    count += 1
                    if count == count2:
                        break

else:
    for i in pslovar:
        for j in pslovar[i]:
            if endTmp[0] in j:
                pEnd.append(i)
pEnd = set(pEnd)
print(pEnd)

while True:
    cepochka = input("Введите цепочку: ").split()
    current = p2slovar[0]
    flag = True
    for i in cepochka:
        if plist[current][i] == set():
            print("Автомат не допускает эту цепочку")
            flag = False
            break
        else:
            current = plist[current][i]
    if flag == True:
        if current in pEnd:
            print('Автомат допускает эту цепочку')
        else:
            print('Автомат не допускает эту цепочку')
