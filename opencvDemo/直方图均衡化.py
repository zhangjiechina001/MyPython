import cv2

src=cv2.imread('circle.jpg',cv2.IMREAD_GRAYSCALE)
def equalize(src):
    dst=cv2.equalizeHist(src)
    return dst

cv2.imshow('equalizeHist',equalize(src))
cv2.waitKey()