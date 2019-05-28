import cv2

src=cv2.imread('bestimg.jpg')
src=src[30:90,:,]
cv2.imshow('src',src)
cv2.waitKey()
cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.imwrite('cut1.jpg',src)
cv2.destroyAllWindows()