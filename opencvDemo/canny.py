import cv2
def main():
    src=cv2.imread('Itality.jpg')
    cv2.imshow('sec',src)
    res=cv2.Sobel(src,3,3,2)
    cv2.waitKey()

main()