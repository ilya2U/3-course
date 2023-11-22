from collections import Counter
import base64
from PIL import Image, ImageFile 
import io
import re
from PIL import Image

file = open('text.txt', 'r')
decodedText = file.read()
file.close()
print(decodedText)


def decode_76(data, altchars=b'+/'):
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)

bib = decodedText.encode("ASCII")
print(bib)
b = base64.b64decode(bib)
imag = Image.open(io.BytesIO(b))
imag.show()
print(b)



