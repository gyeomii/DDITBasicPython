import cv2

img1 = cv2.imread('image/Lenna.png')

print('img1', type(img1))

print('img1', img1)

cv2.imshow('Lenna1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()