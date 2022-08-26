import numpy as np
import cv2

xml = 'cascade/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(xml)
img = cv2.imread('image/startup.png')
peng = cv2.imread('image/Pengsu.png', cv2.IMREAD_UNCHANGED)

trans_mask = peng[:,:,3] == 0
gray = cv2.cvtColor(peng, cv2.COLOR_BGRA2GRAY)
trans_mask = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
alpha = peng[:,:,3] # Channel 3
result = np.dstack([trans_mask, alpha])

faces = face_cascade.detectMultiScale(img,1.05,5) 
print("Number of faces detected: " + str(len(faces)))

if len(faces):
    for (x,y,w,h) in faces:
        face_img = cv2.resize(result, (w, h), interpolation=cv2.INTER_AREA) # 확대
        img[y:y+h, x:x+w] = face_img # 인식된 얼굴 영역 모자이크 처리

cv2.imshow('result', img)
        
k = cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 파일