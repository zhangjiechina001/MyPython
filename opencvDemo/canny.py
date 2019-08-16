import cv2
img=cv2.imread('DPlayer.png')
cv2.imshow('img',img)
res=cv2.Canny(img,20,30,edges=2)
cv2.imshow('res',res)
cv2.waitKey()