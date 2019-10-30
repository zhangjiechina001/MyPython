import cv2
import numpy as np

img=cv2.imread('Itality.jpg')
mask = np.zeros(img.shape, np.uint8)
drawFlag = False
imgcopy=img.copy()
def draw_circle(event, x, y, flags, param):
    #EVENT_LBUTTONDOWN
    global drawFlag
    global imgcopy
    global mask
    if (event==cv2.EVENT_LBUTTONDOWN):
        drawFlag=True
    if (event==cv2.EVENT_LBUTTONUP):
        drawFlag=False
    if (event==cv2.EVENT_MOUSEMOVE)&drawFlag:
        cv2.circle(imgcopy, (x, y), 5, (255, 255, 0), -1)
        cv2.circle(mask, (x, y), 5, (255, 255, 255), -1)
    if(event==cv2.EVENT_RBUTTONDOWN):
        imgcopy=repir_pic(imgcopy,mask=mask)
    cv2.imshow('image',imgcopy)

def repir_pic(img,mask):
    mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    dst=cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
    return dst


cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.setMouseCallback('image', draw_circle)


# while (1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
cv2.waitKey()
cv2.destroyAllWindows()

# import cv2
# def On_Mouse()