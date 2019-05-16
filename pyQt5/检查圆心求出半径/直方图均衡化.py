import cv2

src=cv2.imread('bestimg.jpg',cv2.IMREAD_GRAYSCALE)
src=cv2.equalizeHist(src)
cv2.imshow('result',src)
cv2.waitKey()
cv2.imwrite('afterEqualize.jpg',src)
cv2.destroyAllWindows()