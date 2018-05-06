import cv2
import numpy as np
from Graph import *

lower_red = np.array([0, 100, 100])
upper_red = np.array([255, 255, 255])
Circle = Place()
status = "No circles found"

cap = cv2.VideoCapture(0)
ret, _ = cap.read()  # Checking connection

while ret:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1024, 768))

    # cv2.imwrite("Frames\\frame.jpg", frame)  # save frame as JPEG file
    # img = cv2.imread('Frames\\frame.jpg', 0)
    # img = cv2.medianBlur(frame, 5)
    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # cimg = img

    # img = cv2.imread("Frames\\frame.jpg", 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    #cv2.imshow('mask', mask)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 600, param1=200, param2=40, minRadius=50, maxRadius=0)
    try:
        circles = np.uint16(np.around(circles))
    except AttributeError:
        pass

    try:
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    except TypeError:
        pass

    if circles is not None:
        NumberOfCircles = circles.shape[1]
        if NumberOfCircles == 1:
            for i in circles[0, :]:
                Circle.x = i[0]
                Circle.y = i[1]
                Circle.z = i[2]
            status = ('%s %s' % (NumberOfCircles, 'circle'))
        elif circles.shape[1] > 1:
            status = ('%s %s' % (NumberOfCircles, 'circles'))
    elif circles is None:
        status = "No circles found"
        Circle.x = None
        Circle.y = None
        Circle.z = None

    cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('detected circles', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
