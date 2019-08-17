import cv2
src=cv2.imread('Itality.jpg')
cv2.imshow('src',src)
def DoubleCallBack(value):
    para = value
    res = cv2.bilateralFilter(src, para, para * 2, para // 2)
    cv2.imshow('res', res)

def DoubleCallBack1(value):
    if(value%2==1):
        para=value
    else:
        para=value+1
    # kernel = cv2.getGaussianKernel(value,1)
    res=cv2.GaussianBlur(src,(para,para),0)
    cv2.imshow('src', res)

cv2.namedWindow('res',cv2.WINDOW_NORMAL)
cv2.createTrackbar('size','res',20,200,DoubleCallBack)
cv2.createTrackbar('size','src',20,50,DoubleCallBack1)
cv2.imshow('res', src)
cv2.waitKey()





