import cv2

WINNAME='src'
src=cv2.imread('haku.png',cv2.IMREAD_GRAYSCALE)
def callback(x,img=src):
    cannyImg=cv2.Canny(img,x,255)
    image, contours, hierarchy = cv2.findContours(cannyImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mu=[0 for i in range(len(contours))]
    mc=[0 for i in range(len(contours))]
    for i in range(len(contours)):
        mu[i]=cv2.moments(contours[i])
        temp=mu[i]
        mc[i]=(int(temp['m10']/temp['m00']),int(temp['m01']/temp['m00']))
        print(mc[i])
    return

cv2.imshow(WINNAME,src)
cv2.createTrackbar('value',WINNAME,100,255,callback)
cv2.waitKey()
