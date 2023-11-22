import json
import base64
from PIL import Image
import io
from collections import Counter

def b_encode(image):
    with open(image,'rb') as f:
        binar = base64.b64encode(f.read())
        f.close()
    return binar

image = "file.bmp"
bibib = b_encode(image)
print(bibib)
b = bibib.decode("ASCII")
print(type(b))

file = b

f = open('text.txt', 'w')
for i in file:
    f.write(i)
