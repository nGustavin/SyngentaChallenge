# Tentando inverter as cores da imagem procurando mensagens escondidas. (Não deu certo)
# import matplotlib.pyplot as plt
# import numpy as np

# img = plt.imread("Syngenta.bmp")
# plt.imshow(np.invert(img))

# -----------------------------------------------------------------------------------------


# Tentando Steganography(Nao deu certo)

import cv2

img = cv2.imread('image.bmp', cv2.IMREAD_GRAYSCALE)
i = 0
bits = ''
chars = []
for row in img:
    for pixel in row:
        bits = str(pixel & 0x01) + bits
        i += 1
        if(i == 8):
            chars.append(chr(int(bits, 2)))
            i = 0
            bits = ''

print(''.join(chars))


# -----------------------------------------------------------------------------------------


# Mais Steganography...(Nao deu certo)

# import cv2

# def get_image(image_location):
#   img = cv2.imread(image_location)
#   return img

# def gcd(x, y):
#   while(y):
#     x, y = y, x % y

#   return x

# def decode_image(img_loc):
#   img = get_image(img_loc)
#   pattern = gcd(len(img), len(img[0]))
#   message = ''
#   for i in range(len(img)):
#     for j in range(len(img[0])):
#       if (i-1 * j-1) % pattern == 0:
#         if img[i-1][j-1][0] != 0:
#           message = message + chr(img[i-1][j-1][0])
#         else:
#           return message


# get_image("./example.bmp")
# decode_image("./example.bmp")


# -----------------------------------------------------------------------------------------

