import itertools
k1 = list(itertools.product('abc', repeat=2))+list(itertools.product('abc', repeat=3))+list(itertools.product('abc', repeat=4))+list(itertools.product('abc', repeat=5))
print('\nСписок всех цепочек\n', k1)
h = []
for el in k1:
    k=0
    for j in range(len(el)-1):

        if  el[j] + el[j + 1] == 'cb':
            k=1
            break
    if el[0] == 'a' and el[-1] == 'c' and k==0:
      h.append(el)



temp = []
for x in h:
    if x not in temp:
        temp.append(x)
h = temp
print('\nСписок цепочек, не содержащий сb, начинается на "a" и заканчивается на "c"\n', h)




##   ^a [^bc ] ^b