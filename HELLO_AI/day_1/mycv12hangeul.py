import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = cv2.imread('../day17/image/startup.png')
# cv2 -> PIL 이미지로 변경
color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_pil=Image.fromarray(color_coverted)

# PIL 이미지에 한글 입력
draw = ImageDraw.Draw(img_pil)
draw.text((380, 150),  "수지", font=ImageFont.truetype("font/MALGUN.TTF", 48), fill=(255,255,255))

# PIL 이미지 -> cv2 Mat 타입으로 변경
numpy_img = np.array(img_pil)

cv_img = cv2.cvtColor(numpy_img, cv2.COLOR_RGB2BGR)

cv2.imshow('startup' , cv_img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 