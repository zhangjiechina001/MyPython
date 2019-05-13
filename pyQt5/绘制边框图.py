import cv2


# 寻找最大轮廓，传入的是一个二值的黑白图
def FindBigestContour(src):
    imax = 0
    imaxcontours = -1
    # 返回的是原图片，边界集合，轮廓的属性
    image, contours, hierarchy = cv2.findContours(src,
                                                  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        itemp = cv2.contourArea(contours[i])
        if (imaxcontours < itemp):
            imaxcontours = itemp
            imax = i

    return contours[imax]

src=cv2.imread('bestimg.jpg')
src=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
_,src=cv2.threshold(src,150,255,cv2.THRESH_BINARY)
maxContour=FindBigestContour(src)
maxRect=cv2.boundingRect(maxContour)
src=cv2.drawContours(src,maxContour,-1,color=(255,190,200))
cv2.imshow('result',src)
cv2.waitKey()
cv2.destroyAllWindows()