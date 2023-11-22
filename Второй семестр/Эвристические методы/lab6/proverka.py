n = 4
m = 12
string = "12 9 10 16 19 8 13 18 15 9 12 14 11 18 12 9 20 7 10 19 20 10 15 17 19 11 10 20 18 16 20 11 16 18 11 8 8 12 8 19 10 17 16 18 16 16 19 19 "
def go(stroka):
    def convert_string_to_array(string, n, m):
        # Разделить строку на отдельные числа
        numbers = string.split()
        # Проверить, достаточно ли чисел для создания двумерного массива
        if len(numbers) != n * m:
            raise ValueError("Неверное количество чисел для создания массива")
        # Создать двумерный массив размером n x m
        array = [[0] * m for _ in range(n)]
        # Заполнить массив числами из строки
        for i in range(n):
            for j in range(m):
                index = i * m + j
                array[i][j] = int(numbers[index])
        return array

    def print_2d_array(array):
        for row in array:
            print(' '.join(str(element) for element in row))

    result = convert_string_to_array(string, n, m)
    print_2d_array(result)

    numbers = stroka.split()
    array = [int(num) for num in numbers]

    fin = [[0] * m for _ in range(n)]  # финальный массив 
    def find_interval(number):
        siz = 257 // n  # Размер каждого отрезка

        for i in range(n):
            start = i * siz 
            end = (i + 1) * siz

            if number >= start and number < end:
                return i

    for i in range(len(array)):

        b = find_interval(array[i])
        for j in range(len(array)):
            if fin[b][j] == 0:
                fin[b][j] = result[b][i]
                break

    for i in range(n):
        print(fin[i], sum(fin[i]))

go("226  	2  	89  	187  	166  	73  	167  	85  	3  	38  	139  	166")
go("226	2	89	123	166	73	167	85	3	38	139	166")

print("         ")