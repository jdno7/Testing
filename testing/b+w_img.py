import cv2

#reads and converts img to grayscale
im_gray = cv2.imread('test.jpeg', cv2.IMREAD_GRAYSCALE)
#defines the threshold automatically
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#save img
cv2.imwrite('bw_image.jpeg', im_bw)