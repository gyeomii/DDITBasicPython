import cv2

img = cv2.imread('image/startup.png')
imgRsize = cv2.resize(img, (500, 300))
cv2.imshow('rotate45',imgRsize)
cv2.imwrite('image/startup_resize.jpg', imgRsize)
cv2.waitKey(0)
cv2.destroyAllWindows()