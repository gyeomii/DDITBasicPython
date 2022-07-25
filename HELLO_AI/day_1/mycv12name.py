import cv2

img = cv2.imread('image/startup.png')

# 폰트 색상 지정
blue = (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
white= (255, 255, 255) 
# 폰트 지정
font =  cv2.FONT_HERSHEY_PLAIN
 
# 이미지에 글자 합성하기
img = cv2.putText(img, "SUZY", (400, 170), font, 2, blue, 3, cv2.LINE_AA)
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
# 이미지 보여주고 창 끄기
cv2.imshow('startup' , img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 