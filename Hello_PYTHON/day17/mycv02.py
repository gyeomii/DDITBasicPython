import cv2

img1 = cv2.imread('image/R.png')
img2 = cv2.imread('image/G.png')
img3 = cv2.imread('image/B.png')
print('img1', img1)
print('img2', img2)
print('img3', img3)
cv2.imshow('RGB',img1)

# B [255   0   0]
# G [  0 255   0]
# R [  0   0 255]

cv2.waitKey(0)
cv2.destroyAllWindows()