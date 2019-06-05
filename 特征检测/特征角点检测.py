import cv2
import numpy as np

img=cv2.imread('chess_board.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,29,0.04)
cv2.imshow('gray',dst)
max=dst.max()
img[dst>0.001*max]=[0,255,0]
cv2.imshow('corners',img)
cv2.waitKey()
cv2.waitKey()