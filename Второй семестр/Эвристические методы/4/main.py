import numpy as np
import function

m = int(input("m = "))
n = int(input("n = "))
min_number = int(input("min number = "))
max_number = int(input("max number = "))
matrix = np.random.randint(min_number, max_number, size=(m, n))

print(matrix, "\n")



while 1:
    x = int(input("0 - по убыванию; 1 - по возрастанию; 2 - случайный генератор\n"))
    if x == 0:
        print("метод 2: ", function.fun2(matrix, n, m, 0), "\n")

        print("метод 3: ", function.fun3(matrix, n, m, 0), "\n")

    elif x == 1:
        print("метод 2: ", function.fun2(matrix, n, m, 1), "\n")

        print("метод 3: ", function.fun3(matrix, n, m, 1), "\n")

    elif x == 2:
        print("метод 2: ", function.fun2(matrix, n, m, 2), "\n")

        print("метод 3: ", function.fun3(matrix, n, m, 2), "\n")

    else:
        print("\nНеправильный выбор! Попробуйте снова!\n\n")