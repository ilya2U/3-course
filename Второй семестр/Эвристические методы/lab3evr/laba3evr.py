import random
import copy

m, n = int(input('количество задач: ')), int(input('число устройств: '))
T1, T2 = int(input('от: ')), int(input('до: '))
mas, masP, masSum = [], [], [0] * n

for i in range(n):
    masP.append([])

while len(mas) < m:
    acc = random.randint(T1, T2)
    mas.append(acc)
#mas = [12, 13, 14, 15, 19, 10, 11, 13, 18]
#print(mas)
for i in mas:
    acc = random.randint(0, n - 1)
    masP[acc].append(i)
#masP = [[12, 10, 13], [13, 19, 18], [14, 15, 11]]
#print(masP)
first_modern, second_modern = copy.deepcopy(mas), copy.deepcopy(masP)

print('masP =', masP)

for i in masP:
    for k in masP: masSum[masP.index(k)] = sum(k)
    delt = max(masSum) - min(masSum)
    for j in masP[masSum.index(max(masSum))]:
        if j < delt:
            masP[masSum.index(min(masSum))].append(j)
            masP[masSum.index(max(masSum))].remove(j)
            break

print()
print('После сравнения прибора с максимальной нагрузкой с дельта: ')
acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('После сравнений между приборами с наименьшей и наибольшей нагрузкой:')

second, new_prov, acc1, acc2, delt = True, True, -1, -1, max(masSum) - min(masSum)
while second:
    for _ in masP: masSum[masP.index(_)] = sum(_)
    while new_prov:
        masPprov = copy.deepcopy(masP)
        for _ in masP[masSum.index(max(masSum))]:
            if _ < delt:
                masP[masSum.index(min(masSum))].append(_)
                masP[masSum.index(max(masSum))].remove(_)
                for _ in masP: masSum[masP.index(_)] = sum(_)
                delt = max(masSum) - min(masSum)
                break
        if masPprov == masP:
            new_prov = False
    delt = max(masSum) - min(masSum)
    masPprov = copy.deepcopy(masP)
    for i in masP[masSum.index(max(masSum))]:
        acc1 += 1
        for j in masP[masSum.index(min(masSum))]:
            acc2 += 1
            if (i > j) and (i - j < delt):
                masP[masSum.index(max(masSum))][acc1], masP[masSum.index(min(masSum))][acc2] = \
                    masP[masSum.index(min(masSum))][acc2], masP[masSum.index(max(masSum))][acc1]
                acc1, acc2 = -1, -1
                break
        if masPprov != masP:
            break
        else:
            acc2 = -1
            new_prov = True
    else:
        second = False
        break

acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('Max =', max(masSum))

# 1 модификация
print()
print('----1 модификация----')

mas, masSum, masNumbers, masx2 = first_modern, [0] * n, [], []
print(f'mas = {mas}')

for _ in range(n):
    masx2.append([])

print('Mas:')
for i in mas:
    for j in range(n):
        print(i, end=' ')
    print()

print('\nSort:')
mas.sort()
mas.reverse()

for i in mas:
    for j in range(n):
        print(i, end=' ')
    print()

print('\nSums of appliances:')

acc, full_acc = 0, 0
print(*masSum)

while full_acc < m:
    number = mas[full_acc]

    if acc < n:
        masx2[masSum.index(min(masSum))].append(number)
        masSum[masSum.index(min(masSum))] += number
        acc += 1
        full_acc += 1
        print(*masSum)
        continue
    if acc == n:
        masx2[masSum.index(min(masSum))].append(number)
        masSum[masSum.index(min(masSum))] += number
        acc = 1
        full_acc += 1
        print(*masSum)

print(f'\nMas = {mas}')
print(f'End number = {max(masSum)}')
print(f'masx2 = {masx2}')
mas, masP, masSum = [], copy.deepcopy(masx2), [0] * n
print('masP =', masP)
for i in masP:
    for k in masP: masSum[masP.index(k)] = sum(k)
    delt = max(masSum) - min(masSum)
    for j in masP[masSum.index(max(masSum))]:
        if j < delt:
            masP[masSum.index(min(masSum))].append(j)
            masP[masSum.index(max(masSum))].remove(j)
            break
print()
print('Первый шаг: ')
acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('Второй шаг:')
second, new_prov, acc1, acc2, delt = True, True, -1, -1, max(masSum) - min(masSum)
while second:
    for _ in masP: masSum[masP.index(_)] = sum(_)
    while new_prov:
        masPprov = copy.deepcopy(masP)
        for _ in masP[masSum.index(max(masSum))]:
            if _ < delt:
                masP[masSum.index(min(masSum))].append(_)
                masP[masSum.index(max(masSum))].remove(_)
                for _ in masP: masSum[masP.index(_)] = sum(_)
                delt = max(masSum) - min(masSum)
                break
        if masPprov == masP:
            new_prov = False
    delt = max(masSum) - min(masSum)
    masPprov = copy.deepcopy(masP)
    for i in masP[masSum.index(max(masSum))]:
        acc1 += 1
        for j in masP[masSum.index(min(masSum))]:
            acc2 += 1
            if (i > j) and (i - j < delt):
                masP[masSum.index(max(masSum))][acc1], masP[masSum.index(min(masSum))][acc2] = \
                    masP[masSum.index(min(masSum))][acc2], masP[masSum.index(max(masSum))][acc1]
                acc1, acc2 = -1, -1
                break
        if masPprov != masP:
            break
        else:
            acc2 = -1
            new_prov = True
    else:
        second = False
        break
acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('Max =', max(masSum))

# 2 модификация
print('----2 модификация----')
mas, masP, masSum = [], second_modern, [0] * n
print('masP =', masP)
for i in masP:
    for _ in masP: _.sort(reverse = True)
    for k in masP: masSum[masP.index(k)] = sum(k)
    delt = max(masSum) - min(masSum)
    for j in masP[masSum.index(max(masSum))]:
        if j < delt:
            masP[masSum.index(min(masSum))].append(j)
            masP[masSum.index(max(masSum))].remove(j)
            break
print()
print('Первый шаг: ')
acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('Второй шаг:')
second, new_prov, acc1, acc2, delt = True, True, -1, -1, max(masSum) - min(masSum)
while second:
    for _ in masP: _.sort(reverse = True)
    for _ in masP: masSum[masP.index(_)] = sum(_)
    while new_prov:
        masPprov = copy.deepcopy(masP)
        for _ in masP[masSum.index(max(masSum))]:
            if _ < delt:
                masP[masSum.index(min(masSum))].append(_)
                masP[masSum.index(max(masSum))].remove(_)
                for _ in masP: masSum[masP.index(_)] = sum(_)
                delt = max(masSum) - min(masSum)
                break
        if masPprov == masP:
            new_prov = False
    delt = max(masSum) - min(masSum)
    masPprov = copy.deepcopy(masP)
    for i in masP[masSum.index(max(masSum))]:
        acc1 += 1
        for j in masP[masSum.index(min(masSum))]:
            acc2 += 1
            if (i > j) and (i - j < delt):
                masP[masSum.index(max(masSum))][acc1], masP[masSum.index(min(masSum))][acc2] = \
                    masP[masSum.index(min(masSum))][acc2], masP[masSum.index(max(masSum))][acc1]
                acc1, acc2 = -1, -1
                break
        if masPprov != masP:
            break
        else:
            acc2 = -1
            new_prov = True
    else:
        second = False
        break
acc_for_print = 1
for _ in masP:
    print(f'p{acc_for_print} =', *_)
    acc_for_print += 1
print(*masSum)
print()
print('Max =', max(masSum))

