import cv2

img1 = cv2.imread('image/Lenna.png')
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print('dst', dst)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
