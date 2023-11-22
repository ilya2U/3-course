import pandas as pd
import matplotlib.pyplot as plt
import copy

def Determinizciya(slovar):
	print("\nДетерминизация:")
	#Создаем S-ки
	slist = {}
	k = 0
	for i in vershini:
		slist["S" + str(k)] = slovar[i]["E"]
		k += 1
	print("\n",slist,"\n")

	endTmp = []
	count2 = len(slist) - len(end)
	if len(end)>1:
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

	#Создаем словарь с S-ками
	#Итоговый словарь с S-ками {S1:{a:[...],b:[...]...},S2:{...},...Sn:{...}}
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
	PrintSlovar(s2list)

	#Создаем P-шки
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
	#Итоговый словарь с p-шками {p1:{a:[...],b:[...]...},p2:{...},...pn:{...}}
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
				pslovar["P"+str(f)] = n
				tmpslov[k] = "P"+str(f)
				p2slovar.append("P"+str(f))
				f += 1
		plist["P"+str(w)] = tmpslov
		w += 1
	print("\nДетерминированный автомат:\n")
	print(pslovar)
	PrintSlovar(plist)

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
	pEnd = list(set(pEnd))
	CheckCepochka(p2slovar, pEnd, plist)
	hztmp = DelVershiny(plist, p2slovar, pEnd)
	plist = hztmp[0]
	p2slovar = hztmp[1]
	pEnd = hztmp[2]
	Minimizaciya(pEnd, p2slovar,plist)

def Minimizaciya(pEnd, p2slovar,plist):
	print("\nМинимизация:")
	#Разделяем вершины на конечные и не конечные
	tmplist1 = []
	tmplist2 = []
	for i in p2slovar:
		if i not in pEnd:
			tmplist1.append(i)
		else:
			tmplist2.append(i)
	print("\nВершины:\n",tmplist1,"\nКонечные вершины:\n",tmplist2)

	vseVershini = [tmplist1, tmplist2]

	flag = True
	while flag == True:
		vseVershiniCopy = vseVershini.copy()
		checklist = copy.deepcopy(vseVershini) #Сюда сохраняется предыдущая кси
		for bukv in alphavet: #Прогоняем по каждой букве
			print("\nТекущий символ: ",bukv)
			checklist.reverse() #костыль походу
			spisok = 0
			print("Кси-1: ",checklist)
			while spisok < len(vseVershiniCopy):
				if vseVershiniCopy[spisok] != []:
					print(vseVershiniCopy)
					for ksi in checklist: #Прогоняем по всем классам предыдущего кси
						print("Текущий класс кси-1: ",ksi)
						print(vseVershiniCopy)
						tmpVershini = []
						for el in vseVershiniCopy[spisok]: #прогоняем по всем элементам текущего класса
							#если текущий элемент по текущей букве не входит в текущий
							#класс предыдущего кси, то добавляем его во временный список
							if plist[el][bukv] not in ksi:
								print("Элемент: ",el)
								tmpVershini.append(el)
						tmpVershini = list(set(tmpVershini))
						tmpVershini.sort()
						if len(tmpVershini) > 0:
							#удаляем выпавшие элементы и создаем из них новый класс
							print("Новый класс: ",tmpVershini)
							for i in tmpVershini:
								vseVershini[spisok].remove(i)
							vseVershini.append(tmpVershini)
				else:
					spisok += 1
			for i in vseVershiniCopy:
				if i == []:
					vseVershini.remove(i)
			vseVershiniCopy = vseVershini.copy()
		#сравниваем предыдущую кси с текущей
		print("Сравнение кси: ", checklist, " и " ,vseVershini)
		if checklist == vseVershini or checklist[::-1] == vseVershini:
			flag = False
	newVersini = {}
	newslovar = {}
	for i in vseVershini:
		newVersini[i[0]] = i
	newVersini2 = [i for i in newVersini]
	for i in newVersini:
		tmpslovar = {}
		for buk in alphavet:
			for key, value in newVersini.items():
				if plist[i][buk] in value:
					tmpslovar[buk] = [key]
		newslovar[i] = tmpslovar

	print("\nМинимизированный автомат:\n",vseVershini)
	print(newVersini)
	print(newVersini2)
	PrintSlovar(newslovar)

def CheckCepochka(p2slovar, pEnd, plist):
	flag2 = True
	while flag2:
		a = int(input("Проверить цепочку?(1-да|2-нет)\n"))
		if(a == 1):
			cepochka = input("Введите цепочку(символы через пробел): ").split()
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
		else:
			flag2 = False

def PrintSlovar(slovar):
	df1 = pd.DataFrame(slovar)
	df1 = df1.T
	print(df1)

def DelVershiny(slovar, vershini, end):
	for i in slovar:
		for j in alphavet:
			slovar[i][j] = "".join(slovar[i][j])

	q = 1
	#удаляем недостижимые вершины(если в вершину нет путей из других вершин, удаляем её)
	while q < len(slovar):
		flag = False
		#qtmp - текущая вершина
		#vershini[q] - проверяемая на достижимость вершина
		for qtmp in slovar:
			for buk in alphavet:
				j = slovar[qtmp][buk]
				if j == vershini[q] and qtmp != vershini[q]:
						flag = True
		if flag == False:
			del slovar[vershini[q]]
			if(vershini[q] in end):
				end.remove(vershini[q])
			print("Удалили ",vershini[q])
			vershini.remove(vershini[q])
			q = 1
		else:
			q += 1
	PrintSlovar(slovar)
	return ([slovar, vershini, end])

n = input("Введите алфавит: ")
alphavet = n.split()
print(alphavet)
m = int(input("Введите количество вершин: "))
vershini = ["q" + str(i) for i in range(m)]
start = input("Введите начальную вершину: ")
end = input("Введите конечную вершину: ").split()

#Формирования словаря с q-шками:
slovar = {} #словарь с q-шками
#1)Пользовательский воод
for i in vershini:
	slovar2 = {}
	for j in alphavet:
		print("Куда можно пройти из ",i," по ",j,"?")
		n = input().split()
		slovar2[j] = set(n)
	print("Куда можно пройти из ",i," по E ?")
	f = input().split()
	f.append(i)
	slovar2["E"] = set(f)
	slovar[i] = slovar2
print("Исходный словарь:\n")
PrintSlovar(slovar)

#2)Объединяем значения вершин, соединенных эпсилонами
for i in slovar:
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
print("Исходный словарь:\n")
PrintSlovar(slovar)
#Проверяем на детерминированность(если хоть по одному символу нет пути в вершину, автомат не детерминирован)
flag = False
for q in slovar:
	for buk in alphavet:
		if slovar[q][buk] == set():
			flag = True

if flag:
	Determinizciya(slovar)
else:
	print("Автомат детерминизирован")
	#{q0:{a:[...],b:[...]...},q1:{...},...qn:{...}}
	hztmp = DelVershiny(slovar,vershini,end)
	slovar = hztmp[0]
	vershini = hztmp[1]
	end = hztmp[2]
	print("Конечные вершины: ", end)
	CheckCepochka(vershini, end, slovar)
	Minimizaciya(end,vershini,slovar)
