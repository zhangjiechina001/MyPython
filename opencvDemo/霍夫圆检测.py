import cv2

src = cv2.imread('circle.jpg')
cv2.imshow('src', src)

garry = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('garry', garry)
cv2.namedWindow('result')
# circles = cv2.HoughCircles(garry, cv2.HOUGH_GRADIENT, 1, minDist=100, param1=50, param2=20, minRadius=20, maxRadius=150)
#
# if (circles.size != 0):
#     for circle in circles[0, :]:
#         tempcircle = circle
#         src = cv2.circle(src, (tempcircle[0], tempcircle[1]), tempcircle[2], (0, 0, 255), 2)
#         src = cv2.circle(src, (tempcircle[0], tempcircle[1]), 2, (0, 0, 255), 3)  # 画圆心
#     cv2.imshow('result', src)


def callback(x,temp=src):
    temp=temp.copy()
    circles = cv2.HoughCircles(garry, cv2.HOUGH_GRADIENT, 1, minDist=100, param1=50, param2=20, minRadius=20,
                               maxRadius=x)
    if (circles.size != 0):
        res = None
        for circle in circles[0, :]:
            tempcircle = circle
            res = cv2.circle(temp, (tempcircle[0], tempcircle[1]), tempcircle[2], (0, 0, 255), 2)
            res = cv2.circle(temp, (tempcircle[0], tempcircle[1]), 2, (0, 0, 255), 3)  # 画圆心
    cv2.imshow('result', res)

# cv2.createTrackbar('B', 'image', 0, 255, callback)
cv2.createTrackbar('value', 'result', 0, 200, callback)
cv2.waitKey()
