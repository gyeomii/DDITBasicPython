import cv2

src = cv2.imread('image/Lenna.png')

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

dst_01 = mosaic(src)

dst_005 = mosaic(src, ratio=0.05)

cv2.imshow('dst_01',dst_01)
cv2.imshow('dst_005', dst_005)
cv2.waitKey(0)
cv2.destroyAllWindows()