#!/usr/local/bin/python3
import numpy as np
import cv2 

img = cv2.imread("Syngenta.bmp")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([10, 10, 10])
upper_range = np.array([70, 255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

greenAmount = cv2.countNonZero(mask)

# Quando rodar o código, ele abrira a imagem original e a imagem processada, 
# para fechar as imagens e ver a quantidade de pixels verdes aperte 0 no teclado

cv2.imshow("Image", img)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Amount of green pixels: {}".format(greenAmount))
