#import time

def lzencode(wind, buf,FileIn,FileOut):
    global l
    file = open(FileIn, 'r', encoding='utf-8')
    text = file.read()
    buffer = []
    window = ["*"]*wind
    for i in range(buf): # добавляем в буфер первые символы
        buffer.append(text[i])
        l = i+1
    f = open(FileOut, 'w',encoding="utf-8")
    check = True
    while check:
        windowstr = "".join(window) #переменные для нахождения подстроки и составления кода
        buffstr = ""
        code = ""
        for i in range(buf-1): #поочерёдно добавляются буквы в буфер и на их основе составляются коды
            buffstr += buffer[i]

            if windowstr.find(buffstr) != -1:
                code = f"{windowstr.find(buffstr)}*{len(buffstr)}*{buffer[i+1]}$"
            else:
                #составление кодов
                if code != "":
                    code = code
                    break
                else:
                    code = "0*" + "0*" + buffstr[0]+"$"
                    break

        for j in range(len(buffstr)):
            #перемещение в словарь найденной подстроки
            window.pop(0)
            window.append(buffer[0])
            buffer.pop(0)
            try:
                buffer.append(text[l])
                if l != len(text)+1: #блок кода для преотвращения ошибок в конце выполнения
                    l += 1
            except:
                continue
        if buffer == []:
           check = False
        f.write(code)
    f.write('\n')
    f.write("#"+str(wind)) #разделитель

def lzdecode(FileIn,FileOut):
    file = open(FileIn, "r",encoding="utf-8")
    text = file.read()
    windind = text.index("#")
    wind = text[windind+1::] #считывание размера окна
    text = text.replace(wind,"")
    wind = ["*"]*int(wind)
    decoded_text = ""

    while True:
        #print(wind)
        try:
            first_sep_ind = text.index("*") #считывание данных для расшифровки
            pos = (text[:first_sep_ind])
            text = text.replace(pos + "*","", 1)
            pos = int(pos)
            second_sep_ind = text.index("*")
            length = (text[0:second_sep_ind])
            text = text.replace(length+"*","",1)
            length = int(length)
            third_sep_ind = text.index("$")
            next_ch = text[0:third_sep_ind]
            text = text.replace(next_ch+"$","",1)
            if (length == 0):
                decoded_text += next_ch
                wind.pop(0)
                wind.append(next_ch)
            else:
                add = []
                for i in range(pos,pos+length):
                    decoded_text+=wind[i]
                    add.append(wind[i])
                decoded_text += next_ch
                for i in range(pos,pos+length):
                    wind.pop(0)
                    wind.append(add[0])
                    add.pop(0)
                wind.append(next_ch)
                wind.pop(0)
        except:
            print("stop")
            file = open(FileOut,"w",encoding="utf-8")
            file.write(decoded_text)
            break


def shfgetfreq(FileIn):
    #функция для подсчёта букв в тексте
    file = open(FileIn, 'r', encoding='utf-8')
    string = file.read()
    Dict = {}
    counter = 0
    for lines in string:
        for i in lines:
            if set(i) <= set(Dict.keys()):
                Dict[i] += 1
            else:
                Dict.update({f'{i}': 1})
            counter += 1
    for keys in Dict.keys():
        Dict[keys] = Dict[keys]/counter
    sorted_tuple = sorted(Dict.items(), key=lambda x: x[1])
    sorted_tuple.reverse()
    Dict = dict(sorted_tuple)
    return Dict

def FreqToList(dict): #превращение словаря в список для удобства работы в дальнейшем
    codeList = []
    for i in dict.keys():
        codeList.append([dict[i],i])
    return codeList

def CodeBeginning(dict):
    codelist = []
    for i in dict.keys():
        codelist.append([i,''])
    return codelist

def codeget(chanses: list, codeList: list, L, R):
    if R - L > 1:
        sum0 = 0
        sum1 = 0
        counter = 0
        #вероятности делятся на две группы, сумарная вероятность первой больше второй, в цикле это выполняется
        #и потом разбивается приписываются коды в список и потом рекурсивно вызывается функция чтобы поделить
        # остальные группы
        for i in range(L, R):
            sum1 += chanses[i][0]

        for i in range(L, R):
            el = chanses[i][0]
            if sum0 < sum1:
                sum0 = sum0 + el
                sum1 = sum1 - el
                counter += 1
            else:
                break
        for i in range(L, L + counter):
            codeList[i][1] = codeList[i][1] + '0'

        for i in range(L + counter, R):
            codeList[i][1] = codeList[i][1] + '1'
        codeget(chanses, codeList, L, L + counter)
        codeget(chanses, codeList, L + counter, R)

    if R - L == 0:
        if L != len(codeList):
            codeList[L][1] = codeList[L][1] + '0'


def ShfEncode(FileIn,FileOut):
    #получаем вероятности
    file = open(FileIn, "r", encoding="utf-8")
    text = file.read()
    #игнорирование строки с окном
    windind = text.index("#")
    wind = text[windind + 1::]
    text = text.replace(wind, "")
    file.close()
    #подсчет букв в тексте
    code = shfgetfreq(FileIn)
    #из словаря в список
    freq = FreqToList(code)
    codes = CodeBeginning(code)
    #вызов функции построения кодов
    codeget(freq, codes, 0, len(codes))
    codes = dict(codes)
    print(codes)
    encoded_text = ''
    #каждую букву кодируем кодом из словаря и записываем в файл
    for i in text:
        for key in codes.keys():
            if i == key:
                encoded_text = encoded_text + codes[key]
    file = open(FileOut,"w",encoding="utf-8")
    file.write(encoded_text)
    file.write("\n")
    file.write("#" + wind)#запись окна
    file.write(str(code))#и вероятностей


def ShfDecode (FileIn, FileOut):
    file = open(FileIn,"r",encoding="utf-8")
    text = file.read()
    s1 = text.index("#")
    s = text.index("{")
    code1 = text[s1-1:s:] #выделение окна
    code = text[s::] #выделение кодов
    print(code1)
    print(code)
    text = text.replace(code,"")
    print(text)
    text = text.replace(code1, "")
    freq = eval(code)
    code = FreqToList(freq)
    codes = CodeBeginning(freq)
    codeget(code,codes,0,len(codes))
    codes = dict(codes)
    file.close()
    sx = []
    enc_ch = ""
    #для расшифровки в строку приписываются коды и т.к коды однозначно декодируются, то им из словаря
    # кодов подставляется соответствующая им буква
    for ch in text:
        enc_ch += ch
        for dec_ch in codes:
            if codes.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    file = open(FileOut,"w",encoding="utf-8")
    file.write("".join(sx))
    file.write(code1)
    file.close()
    file = open(FileOut, "r", encoding="utf-8")
    text = file.read()
    text = text.replace("#","",1)
    print(text)
    file.close()
    file = open(FileOut, "w", encoding="utf-8")
    file.write(text)



choice = int(input(" 1. кодирование \n 2. декодирование\n"))
origin = "text.txt"
path = "w.txt"
encoded = "w.txt"
decoded = "d.txt"
buff = 50
wind = 100
if (choice == 1):
    lzencode(wind, buff, origin, path)
    ShfEncode(path, path)
if (choice == 2):
    ShfDecode(encoded,decoded)
    lzdecode(decoded,decoded)
