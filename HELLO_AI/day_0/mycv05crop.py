import cv2

img = cv2.imread('image/startup.png')
height, width, channel = img.shape
imgC = img[50:500, 250:700] #height, width

cv2.imshow('crop',imgC)

cv2.waitKey(0)
cv2.destroyAllWindows()