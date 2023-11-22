import numpy as np


def descending(matrix):
    matrix = matrix[matrix[:, 1].argsort()[::-1]]

    return matrix


def ascending(matrix):
    matrix = matrix[matrix[:, 1].argsort()]

    return matrix


def fun2(matrix, n, m, x):
    if x == 0:
        matrix = descending(matrix)
    elif x == 1:
        matrix = ascending(matrix)
    elif x == 2:
        matrix = matrix

    print(matrix)

    t = np.zeros(n)
    t[matrix[0, ].argmin()] = matrix[0, ].min()

    for i in range(1, m):
        p = np.zeros(n)
        for j in range(n):
            p[j] = t[j]**2 + matrix[i, j]**2
        p1 = t + matrix[i, ]
        p_i = p.argmin()
        print(p)

        t[p_i] = p1[p_i]

    print(t)

    return t.max()


def fun3(matrix, n, m, x):
    if x == 0:
        matrix = descending(matrix)
    elif x == 1:
        matrix = ascending(matrix)
    elif x == 2:
        matrix = matrix

    print(matrix)
    t = np.zeros(n)
    t[matrix[0, ].argmin()] = matrix[0, ].min()

    for i in range(1, m):
        p = np.zeros(n)
        for j in range(n):
            p[j] = t[j]**2 + matrix[i, j]**3
        p1 = t + matrix[i, ]
        p_i = p.argmin()

        t[p_i] = p1[p_i]
        print(p)

    print(t)

    return t.max()

