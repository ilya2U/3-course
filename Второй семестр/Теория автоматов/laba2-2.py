import itertools
k1 = list(itertools.product('ab', repeat=2))+list(itertools.product('ab', repeat=3))+list(itertools.product('ab', repeat=4))+list(itertools.product('ab', repeat=5))
print('\nСписок всех цепочек\n', k1)
h = []
for el in k1:
    for j in range(len(el)-1):
        if el[j] == 'a' and el[j+1] == el[j] or el[j] == 'b' and el[j+1] == el[j]:
            h.append(el)
temp = []
for x in h:
    if x not in temp:
        temp.append(x)
h = temp
print('\nСписок цепочек, содержащий хотя бы одну пару рядом стоящих а или в\n', h)
