import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL.ExifTags import TAGS


def plot_rod(img):
# img_scale = [[0 for y in range(1344)] for x in range(1008)]
# # raw image dimensions 3024 x 4032
    image = cv.imread(img)

    image_list = image.tolist()

    rod_x = []
    rod_y = []

    for y_idx, y in enumerate(image_list):
        for x_idx, x in enumerate(y):
            if sum(x) <= 175:
                
                rod_x.append(x_idx)
                rod_y.append(y_idx)
                # rod_x.insert(0,x_idx)
                # rod_y.insert(0,y_idx)

    plt.axis([min(rod_x), max(rod_x), max(rod_y), min(rod_y)-100])

    plt.plot(rod_x,rod_y)

    plt.savefig('newplot.jpeg', dpi=300, bbox_inches='tight')

    # plt.show()
