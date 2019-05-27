import cv2

src=cv2.imread('bestimg.jpg')
src=src[10:66,207:242,]
cv2.imshow('src',src)
cv2.waitKey()
cv2.imwrite('cut6.jpg',src)
cv2.destroyAllWindows()