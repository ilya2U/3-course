import random
import copy
import numpy as np
from prettytable import PrettyTable

mytable = PrettyTable()

m, n = int(input('введите кол-во строк: ')), int(input('введите кол-во столбцов/приборов: '))
T1, T2 = int(input('введите левый край: ')), int(input('введите правый край: '))

mas = []

while len(mas) < m * n:
    acc = random.randint(T1, T2)
    mas.append(acc)

splits = list(np.array_split(mas, m))
splits2, splits3 = copy.deepcopy(splits), copy.deepcopy(splits)
print('\n---СОРТИРОВКА ПО УБЫВАНИЮ---\nMatrix:')

mytable.field_names = []
for i in splits:
    mytable.add_row(i)
print(mytable)

for i in range(m - 1):
    for j in range(m - i - 1):
        if sum(splits[j]) > sum(splits[j + 1]):
            splits[j], splits[j + 1] = splits[j + 1], splits[j]

splits.reverse()
mytable2 = PrettyTable()
mytable2.field_names = []
print('Sort:')
for i in splits:
    mytable2.add_row(i)
print(mytable2)

mass, acc = [], []
for i in splits:
    for j in i:
        acc.append(j)
    mass.append(copy.deepcopy(acc))
    acc = []

masSum, masNumbers = [0] * n, [0] * n
masSum[mass[0].index(min(mass[0]))] += (min(mass[0]))
masNumbers[mass[0].index(min(mass[0]))] += (min(mass[0]))
acc_number, acc_index = 0, 0
print('\n', *masSum)
for i in range(1, len(mass)):
    print(*mass[i])
    masSum = list(map(sum, zip(masSum, mass[i])))
    print('----------\n', *masSum, '\n')
    acc_index = masSum.index(min(masSum))
    acc_number = mass[i][acc_index]
    masNumbers[acc_index] += acc_number
    masSum = copy.deepcopy(masNumbers)
    print(*masSum)

print(f'\nMax number = {max(masSum)}\n---СОРТИРОВКА ПО ВОЗРАСТАНИЮ---\nMatrix:')

mytable = PrettyTable()
mytable.field_names = []
for i in splits2:
    mytable.add_row(i)
print(mytable)

for i in range(m - 1):
    for j in range(m - i - 1):
        if sum(splits2[j]) > sum(splits2[j + 1]):
            splits2[j], splits2[j + 1] = splits2[j + 1], splits2[j]

mytable2 = PrettyTable()
mytable2.field_names = []
print('Sort:')
for i in splits2:
    mytable2.add_row(i)
print(mytable2)

mass, acc = [], []
for i in splits2:
    for j in i:
        acc.append(j)
    mass.append(copy.deepcopy(acc))
    acc = []

masSum, masNumbers = [0] * n, [0] * n
masSum[mass[0].index(min(mass[0]))] += (min(mass[0]))
masNumbers[mass[0].index(min(mass[0]))] += (min(mass[0]))
acc_number, acc_index = 0, 0
print('\n', *masSum)
for i in range(1, len(mass)):
    print(*mass[i])
    masSum = list(map(sum, zip(masSum, mass[i])))
    print('----------\n', *masSum, '\n')
    acc_index = masSum.index(min(masSum))
    acc_number = mass[i][acc_index]
    masNumbers[acc_index] += acc_number
    masSum = copy.deepcopy(masNumbers)
    print(*masSum)

print(f'\nMax number = {max(masSum)}')

print('\n---БЕЗ СОРТИРОВКИ---')
mytable = PrettyTable()
mytable.field_names = []
for i in splits3:
    mytable.add_row(i)
print(mytable)

mass = []
acc = []
for i in splits3:
    for j in i:
        acc.append(j)
    mass.append(copy.deepcopy(acc))
    acc = []

masSum, masNumbers = [0] * n, [0] * n
masSum[mass[0].index(min(mass[0]))] += (min(mass[0]))
masNumbers[mass[0].index(min(mass[0]))] += (min(mass[0]))
acc_number, acc_index = 0, 0
print('\n', *masSum)
for i in range(1, len(mass)):
    print(*mass[i])
    masSum = list(map(sum, zip(masSum, mass[i])))
    print('----------\n', *masSum, '\n')
    acc_index = masSum.index(min(masSum))
    acc_number = mass[i][acc_index]
    masNumbers[acc_index] += acc_number
    masSum = copy.deepcopy(masNumbers)
    print(*masSum)

print(f'\nMax number = {max(masSum)}') 
