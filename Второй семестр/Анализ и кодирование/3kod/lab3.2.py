import numpy as np
from PIL import Image
import base64
import io
import re


def b_encode(image):
    with open(image, 'rb') as f:
        binar = base64.b64encode(f.read())

    return binar


def Encode(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    # общее количество пикселей
    total_pixels = array.size // n
    #Всанка барьера (Указателя на конец вшиваемого фото)
    message += "$t3g0"
    # Перевод в двоичный код
    b_message = ''.join([format(ord(i), "08b") for i in message])
    # Количество необходимого количества пикселей
    req_pixels = len(b_message)
    # Проверка на достаточность места в исходном изображении
    if req_pixels > total_pixels:
        print("ОШИБКА: НЕХВАТКА МЕСТА")

    # Замена младших битов на биты вшиваемого изображения !!!!!
    else:
        index = 0
        x = total_pixels -1
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[x][q] = int(bin(array[x][q])[2:9] + b_message[index], 3)
                    index += 1
            x -= 1
    # Создание и сохранение полученного изображения
        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("ГОТОВО")


def Decode(src):
    # КАК В ДЕКОДЕ----------------------
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size // n
    #-----------------------------------
    # Извлечение младших битов и преобразование в ASCII до барьера
    hidden_bits = ""
    x = total_pixels - 1
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[x][q])[2:][-1])
        x -= 1
    hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        bib = message.encode("ASCII")
        B = decode_76(bib)
        imag = Image.open(io.BytesIO(B))
        imag.show()


def decode_76(data, altchars=b'+/'):
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


def Stego():
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        image = "cod.bmp"
        bi = b_encode(image)
        #print(type(bi))
        #print(bi)
        b = bi.decode("ASCII")
        print("Введите путь к исходному изображению")
        src = input()
        print("Введите сообщение, чтобы скрыть")
        message = b
        print("Введите путь к целевому изображению")
        dest = input()
        print("КОДИРОВАНИЕ...")
        Encode(src, message, dest)

    elif func == '2':
        print("Введите путь к исходному изображению")
        src = input()
        print("ДЕКОДИРОВАНИЕ...")
        Decode(src)

    else:
        print("!!!ОШИБКА!!!")


Stego()