import cv2
import numpy as np
import sys

imgpath='Itality.jpg'
img=cv2.imread(imgpath)
gary=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SURF_create(hessianThreshold=5000)
keypoints,desciptor=sift.detectAndCompute(gary,None)
img=cv2.drawKeypoints(image=img,outImage=img,keypoints=keypoints,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,color=(0,0,255))
cv2.imshow('sift_keypoints',img)
cv2.waitKey()
cv2.destroyAllWindows()