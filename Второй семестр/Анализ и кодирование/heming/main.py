import math

#перевод из десятичной в двоичную
def decimalToBinary(n,res = ""):
    if (n >= 1):
        res = str(n%2) + res
        return decimalToBinary(n // 2, res)
    else:
        return res


def encode(length, word: str):
    index = 0
    pow = 0
    index = int(math.pow(2,pow))
    #вставка контрольных битов (вставляются пока индекс следующего бита меньше длины)
    while index < length + 1:
        pow += 1
        length += 1
        temp = []
        #делается это через список
        for char in word:
            temp.append(char)
        temp.insert(index-1, "0")
        word = temp
        index = int(math.pow(2, pow))
    print("слово с контрольными битами:", "".join(word))
    print("матрица преобразования")
    bits = []
    for i in range (length):
        bits.append(int(word[i]))
    res = []
    matrix = []
    for j in range (length):
        matrix.append([])
    #номер каждого столбика (начинается с 1) переводим в двоичную систему и переворачиваем
    for i in range(length):
        num = decimalToBinary(i+1)
        if len(num) < pow:
            #дополняем до одинаковой длины
           while len(num) != pow:
                 num = "0" + num
        for j in range(pow):
            matrix[i].append(int(num[pow-j-1]))
    for i in range(length):
        print(matrix[i])
    #считаем скалярное произведение для каждой строчки (произведение слова и строки матрицы преобразования)
    for j in range(pow):
        scalar = 0
        for i in range(length):
            scalar += int(bits[i]) * int(matrix[i][j])
        scalar = scalar%2
        res.append(scalar)
    #меняем устанваливаем получившиеся контрольные биты
    for j in range(pow):
        bits[int(math.pow(2,j)-1)] = res[j]
    for i in range(len(bits)):
        bits[i] = str(bits[i])
    print("таблица контрольных битов", res)
    print("закодирование слово: ", "".join(bits))

def decode(word):
    length = len(word)
    size = 0
    pow = 0
    #с матрицей делается всё тоже самое
    while size < length:
        pow += 1
        size = int(math.pow(2,pow))
    print("матрица преобразования")
    bits = []
    for i in range(length):
        bits.append(int(word[i]))
    res = []
    matrix = []
    for j in range(length):
        matrix.append([])

    for i in range(length):
        num = decimalToBinary(i + 1)
        if len(num) < pow:
            while len(num) != pow:
                num = "0" + num
        for j in range(pow):
            matrix[i].append(int(num[pow - j - 1]))
    for i in range(length):
        print(matrix[i])
    for j in range(pow):
        scalar = 0
        for i in range(length):
            scalar += int(bits[i]) * int(matrix[i][j])
        scalar = scalar % 2
        res.append(scalar)
    print("синдромы", res)
    #смотрим, все ли числа в матрице синдромов равны 0
    dec = 0
    for i in range(pow):
        dec += int(math.pow(2,i)) * res[i]
    if dec == 0:
        #если это так то просто убираем контрольные биты
        pows = []
        for i in range(pow):
            pows.append(int(math.pow(2,i)))
        number = []
        for i in range(length):
            if i+1 not in pows:
                number.append(bits[i])
        decoded = ""
        for i in number:
            decoded += str(i)
        print(f"раскодированное слово: {decoded}")
    else:
        #иначе инвертируем бит на найденной позиции
        #(находится посредством перевода числа из таблицы синдромов в десятичную)
        print(f"ошибка в {dec} позиции")
        if bits[dec-1] == 0:
            bits[dec-1] = 1
        else:
            bits[dec-1] = 0
        #и так же удаляем контрольные биты
        temp = []
        for i in range(len(bits)):
            temp.append(str(bits[i]))
        print("исправленное слово: ", "".join(temp))
        pows = []
        for i in range(pow):
            pows.append(int(math.pow(2, i)))
        number = []
        for i in range(length):
            if i + 1 not in pows:
                number.append(bits[i])
        decoded = ""
        for i in number:
            decoded += str(i)
        print(f"раскодированное слово: {decoded}")



length = 0
word = ""

while True:
    print("1. Закодировать 2. Раскодировать")
    option = input()
    if option == "1":
        print("введите длину кодируемого слова")
        length = int(input())
        print("введите слово")
        word = input()
        if len(word) > length:
            word = word[0:length+1]
        elif len(word) < length:
            length = len(word)
        encode(length,word)

    elif option == "2":
        print("введите слово")
        word = input()
        decode(word)
