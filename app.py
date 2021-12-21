import cv2 as cv
import numpy as np



# Load the aerial image and convert to HSV colourspace
image = cv.imread("test3.png")
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
black_lo=np.array([0,0,0])
black_hi=np.array([225,225,225])

# Mask image to only select browns
mask=cv.inRange(hsv,black_lo,black_hi)

# Change image to red where we found brown
image[mask>0]=(0,0,255)

cv.imwrite("result.png",image)