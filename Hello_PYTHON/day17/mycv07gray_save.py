import cv2

img = cv2.imread('image/Lenna.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Lenna1',imgGray)
cv2.imwrite('image/Lenna_Gray.jpg',imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()