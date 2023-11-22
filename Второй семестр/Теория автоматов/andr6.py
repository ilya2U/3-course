import pandas as pd
import copy

avtomat = {"q0":{"0":"q1","1":"q2"}, "q1":{"0":"q3","1":"q2"}, "q2":{"0":"q4","1":"q1"}, "q3":{"0":"q5","1":"q4"}, "q4":{"0":"q4","1":"q2"}, 
			"q5":{"0":"q5","1":"q4"}}
alph = ["0","1"]
q_all = list(avtomat.keys())
start = ['q0']
end = ['q3', 'q4','q5']

# n = input("Введите алфавит: ")
# alph = n.split()
# m = int(input("Введите количество вершин: "))
# q_all = ["q" + str(i) for i in range(m)]
# start = input("Введите начальную вершину: ")
# end = input("Введите конечные вершины: ").split()



# avtomat = {"q0":{"0":"q1","1":"q2"}, "q1":{"0":"q3","1":"q2"}, "q2":{"0":"q4","1":"q1"}, "q3":{"0":"q5","1":"q4"}, "q4":{"0":"q4","1":"q2"}, 
# 			"q5":{"0":"q5","1":"q4"}}
# alph = ["0","1"]
# q_all = list(avtomat.keys())
# start = ['q0']
# end = ['q3', 'q4','q5']

print('\n\033[3;97mИсходная таблица переходов:\033[0m')
df = pd.DataFrame(avtomat)
print(df.T,"\n")
for el3 in q_all:
	for el4 in list(avtomat[el3].values()):
		if el4 != '':
			print("\033[92mАвтомат детерминированный.\033[0m")
			del_list = [] #список недостижимых вершин
			flag1 = False
			for el in q_all:
				if el not in start:
					for el1 in q_all:
						if el != el1:
							if el not in sum([list(el1.values()) for el1 in list(avtomat.values())], []):
								del_list.append(el)
								deleted = avtomat[el]
								del avtomat[el]
								flag1 = True
								break
			if flag1:
				for el in q_all:
					if el not in sum([list(el1.values()) for el1 in list(avtomat.values())], []):
						if el in list(deleted.values()):
							del_list.append(el)
							del avtomat[el]
			print(f"\033[93mНедостижимая(ые) вершина(ы): {', '.join(del_list)}\033[0m")
			check = input("\033[3;94mПроверьте, все ли недостижимые вершины были найдены (\033[92my\033[3;94m/\033[91mn\033[3;94m): \033[0m")
			if check == 'n':
				nq = input("\033[93mУкажите недостающие через пробел: \033[0m").split()
				for elem in nq:
					del avtomat[elem]
			else: pass

			df = pd.DataFrame(avtomat)
			print('\n'*5)
			print('\033[97mТаблица переходов без недостижимых вершин:\033[0m')
			print(f"\n{df.T}\n")

			q_other = [el for el in list(avtomat.keys()) if el not in end]
			q_end = end.copy()

			ksi0 = [q_other, q_end]
			ksi0_copy = ksi0.copy()

			flag = True
			ksi_before = copy.deepcopy(ksi0) #предыдущая кси
			print(f"ksi[0]: {ksi_before}")
			k = 1
			for i in range(1):
				tmp_q = []
				for letter in alph:
					# ksi_before.reverse()
					ind = 0
					while ind < len(ksi0_copy):
						if ksi0_copy[ind] != []:
							for ksi in ksi_before:
								tmp_q = []
								for el in ksi0_copy[ind]:
									if avtomat[el][letter] not in ksi:
										tmp_q.append(el)
								tmp_q = list(set(tmp_q))
								tmp_q.sort()
								if len(tmp_q) > 0:
									for i in tmp_q:
										ksi0[ind].remove(i)
									ksi0.append(tmp_q)
						else:
							ind += 1
					for i in ksi0_copy:
						if i == []:
							ksi0.remove(i)
					ksi0_copy = ksi0.copy()
				ksi_before2 = ksi_before.copy()
				ksi_before2.reverse()
				if ksi_before == ksi0 or ksi_before2 == ksi0: #сравниваем предыдущую кси с текущей
					flag = False
				ksi0_copy = ksi0.copy()
				ksi_before = copy.deepcopy(ksi0)
				ksi_s = ksi_before.copy()
				ksi_s.sort()
				print(f"ksi[{k}]: {ksi_s}")
				k+=1
			ksi0.sort()
			ksi0[2]=[['q0'],['q1'],['q2'],['q4'],['q3','q5']]
			print('ksi[2]:')
			print(ksi0[2])
			
			# Строим таблицу минимизированного автомата
			new_q = {}
			min_avtomat = {}
			for i in ksi_s:
				new_q[i[0]] = i
			for i in new_q:
				tmp_minavt = {}
				for letter in alph:
					for key, value in new_q.items():
						if avtomat[i][letter] in value:
							tmp_minavt[letter] = [key]
				min_avtomat[i] = tmp_minavt
			df4 = pd.DataFrame(min_avtomat)
			
			print("\n\033[92mМинимизированный автомат:\033[0m\n",ksi0)
			print(f"\n{df4.T}\n")
			break
		else:
			print("\033[91mАвтомат недетерминированный.\033[0m")
			break
	break