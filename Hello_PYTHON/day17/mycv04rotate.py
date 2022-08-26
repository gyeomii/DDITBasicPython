import cv2


img = cv2.imread('image/startup.png')
height, width, channel = img.shape
M1 = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
img45 = cv2.warpAffine(img, M1, (width, height))
cv2.imshow('rotate45',img45)

cv2.waitKey(0)
cv2.destroyAllWindows()###