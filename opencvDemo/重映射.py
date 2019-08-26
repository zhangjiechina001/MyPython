# import cv2
# import numpy as np
# im=cv2.imread('Itality.jpg')
# cv2.imshow('Itality',im)
# rows,cols,channels=im.shape
# img_x=np.zeros((rows,cols),np.uint8)
# img_y=img_x.copy()
# for y in range(rows):
#     for x in range(cols):
#         img_y[y,x]=rows-y
#         img_x[y,x]=cols-x
#
# remap = cv2.remap(im, img_x, img_y, interpolation=cv2.INTER_CUBIC)
#
# cv2.imshow('remap',remap)
# cv2.waitKey()
import cv2
import numpy as np

src = cv2.imread('Itality.jpg')


def trans(src):
    # 坐标映射
    rows, cols, channels = src.shape

    img_x = np.zeros((rows, cols), np.float32)
    img_y = np.zeros((rows, cols), np.float32)
    for y in range(rows):
        for x in range(cols):
            if x>cols//2:
                img_y[y, x] = rows - y
                img_x[y, x] = cols-x
            else:
                img_y[y, x] =  y
                img_x[y, x] = x
    dst = cv2.remap(src, img_x, img_y, cv2.INTER_LINEAR)
    return dst

def resize(src):
    # 坐标映射
    rows, cols, channels = src.shape

    img_x = np.zeros((rows, cols), np.float32)
    img_y = np.zeros((rows, cols), np.float32)
    for y in range(rows):
        for x in range(cols):
            img_y[y, x] = rows-y
            img_x[y, x] = x
    dst = cv2.remap(src, img_x, img_y, cv2.INTER_LINEAR)
    return dst


dst=resize(src)

# dst = cv2.remap(src,img_x,img_y,cv2.INTER_LINEAR)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()
