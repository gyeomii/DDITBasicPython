import cv2

img = cv2.imread('image/startup.png')

blur = cv2.GaussianBlur(img, (15,15), 0)

"""
cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
src: 입력 영상
ksize: 커널 크기 (주로 홀수)
sigmaX: X 방향 표준편차 (0: auto)
sigmaY(optional): Y 방향 표준편차 (default: sigmaX)
borderType(optional): 외곽 테두리 보정 방식
"""

cv2.imshow('Lenna1',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()