import copy
import numpy as np

n = 12
m = 3
t = np.array([
    [11, 12, 13],
    [18, 17, 16],
    [15, 19, 20],
    [14, 15, 19],
    [20, 14, 11],
    [10, 20, 15],
    [13, 18, 15],
    [14, 10, 12],
    [20, 16, 17],
    [22, 14, 12],
    [17, 20, 19],
    [14, 21, 22]], dtype='int') 
# np.random.randint(8, 16, (n, m))


def printarr_sum(arr):
    for row in arr:
        print(f"{row}  {sum(row)}")
    print()

def strsum_sort_down(a):
    arr = copy.deepcopy(a)
    row_sum_arr = []
    t1 = np.zeros((n, m), 'int')
    for row in arr:
        row_sum_arr.append(sum(row))
    for i in range(len(row_sum_arr)):
        max_ind = row_sum_arr.index(max(row_sum_arr))
        t1[i] = arr[max_ind]
        row_sum_arr.pop(max_ind)
        arr = np.delete(arr, (max_ind), axis=0)
    return t1


def alg33(a):
    matr = copy.deepcopy(a)
    a = [0 for i in range(m)]
    ind = 0
    for i in range(n):
        t = [a.copy() for i in range(m)]
        j = 0
        for i1 in range(m):
            while j < m:
                t[i1][j] = t[i1][j] + matr[i][j]
                j += 1
                break
        t = [[el**2 for el in row] for row in t]
        # print(t)
        sum_t = [sum(t[k]) for k in range(m)]
        print(sum_t)
        ind = sum_t.index(min(sum_t))
        a[ind] += matr[i][ind]
        print(a)
    print(f"Результат: {max(a)}\n\n")


print(f"\nИсходная матрица:")
printarr_sum(t)
alg33(t)

t1 = strsum_sort_down(t)
print(f"Упорядоченная по убыванию сумм строк матрица:")
printarr_sum(t1)
alg33(t1)

t2 = np.flipud(t1)
print(f"Упорядоченная по возрастанию сумм строк матрица:")
printarr_sum(t2)
alg33(t2)
