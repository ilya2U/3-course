import struct
import cv2
import numpy as np

#Задание 1

bmp = open('file.bmp', 'rb')
print('Type:', bmp.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp.read(4)))
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
print('Offset: %s' % struct.unpack('I', bmp.read(4)))
print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
print('Width: %s' % struct.unpack('I', bmp.read(4)))
print('Height: %s' % struct.unpack('I', bmp.read(4)))
print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))


#Задание 2
gray_image = cv2.imread(r'kartinka.bmp', cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread(r'RGB_Colour_Model.bmp')
cv2.imshow('Color all', color_image)
cv2.imshow('Gray all', gray_image)

r1 = cv2.bitwise_and(color_image,(255, 0, 0))
r2 = cv2.bitwise_and(color_image,(0, 255, 0))
r3 = cv2.bitwise_and(color_image,(0, 0, 255))
cv2.imshow('1', r1)
cv2.imshow('2', r2)
cv2.imshow('3', r3)
# cv2.waitKey(0)
#Задание 3
resultImg1g = cv2.bitwise_and(gray_image, (128))
resultImg2g = cv2.bitwise_and(gray_image, (64))
resultImg3g = cv2.bitwise_and(gray_image, (32))
resultImg4g = cv2.bitwise_and(gray_image, (16))
resultImg5g = cv2.bitwise_and(gray_image, (8))
resultImg6g = cv2.bitwise_and(gray_image, (4))
resultImg7g = cv2.bitwise_and(gray_image, (2))
resultImg8g = cv2.bitwise_and(gray_image, (1))

cv2.imshow('bitwise1g', resultImg1g)
cv2.imshow('bitwise2g', resultImg2g)
cv2.imshow('bitwise3g', resultImg3g)
cv2.imshow('bitwise4g', resultImg4g)
cv2.imshow('bitwise5g', resultImg5g)
cv2.imshow('bitwise6g', resultImg6g)
cv2.imshow('bitwise7g', resultImg7g)
cv2.imshow('bitwise8g', resultImg8g)

cv2.waitKey(0)


