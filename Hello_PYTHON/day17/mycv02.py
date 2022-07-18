import cv2

img1 = cv2.imread('B.png')
print('img1', type(img1))
print('img1', img1)
cv2.imshow('RGB',img1)

# B [255   0   0]
# G [  0 255   0]
# R [  0   0 255]

cv2.waitKey(0)
cv2.destroyAllWindows()