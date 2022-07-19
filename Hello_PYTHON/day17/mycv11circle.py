import cv2

img = cv2.imread('image/Lenna.png')

cv2.circle(img, (300,300), 100, (0,0,255), 2)
cv2.imshow('Lenna',img)

cv2.waitKey(0)
cv2.destroyAllWindows()