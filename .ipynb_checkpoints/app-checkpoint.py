#!/usr/local/bin/python3
import numpy as np
import cv2 
# from PIL import Image

# # Open image and make RGB and HSV versions
# RGBim = Image.open("./Syngenta.bmp").convert('RGB')
# HSVim = RGBim.convert('HSV')

# # Make numpy versions
# RGBna = np.array(RGBim)
# HSVna = np.array(HSVim)

# # Extract Hue
# H = HSVna[:,:,0]

# # print(H, RGBna)

# # Find all green pixels, i.e. where 100 < Hue < 140
# lo,hi = 100,140
# # Rescale to 0-255, rather than 0-360 because we are using uint8
# lo = int((lo * 255) / 360)
# hi = int((hi * 255) / 360)
# green = np.where((H>lo) & (H<hi))

# # Make all green pixels black in original image
# RGBna[green] = [0,0,0]

# count = green[0].size
# print("Pixels matched: {}".format(count))

# # Image.fromarray(RGBna).save('result.png')

