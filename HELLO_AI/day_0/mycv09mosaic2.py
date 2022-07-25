import cv2

src = cv2.imread('image/Lenna.png')
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst
"""
     src - 사진 정보

     x - 가로 시작 위치
    
     y - 세로 시작 위치
    
     width - 모자이크 넓이
    
     height - 모자이크 높이
    
     ratio - 모자이크 배율
"""
dst_area = mosaic_area(src, 240, 250, 120, 40)

cv2.imshow('Lenna', dst_area)
cv2.waitKey(0)
cv2.destroyAllWindows()