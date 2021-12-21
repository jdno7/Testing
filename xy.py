import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_scale = [[0 for y in range(1344)] for x in range(1008)]
# raw image dimensions 3024 x 4032
image = cv.imread("test3.png")

image_list = image.tolist()

rod_x = []
rod_y = []

for x_idx, x in enumerate(image_list):
    for y_idx, y in enumerate(x):
        if sum(y) <= 600:
            print(x_idx, y_idx)
            rod_x.append(x_idx)
            rod_y.append(y_idx)


plt.plot(rod_x, rod_y)

plt.show()
