import cv2
import numpy as np

lower_red = np.array([0, 100, 100])
upper_red = np.array([255, 255, 255])

cap = cv2.VideoCapture(0)
ret, _ = cap.read() # Checking connection

while ret:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (660, 440))
    # cv2.imwrite("Frames\\frame.jpg", frame)  # save frame as JPEG file
    # #
    # # img = cv2.imread('Frames\\frame.jpg', 0)
    # img = cv2.medianBlur(frame, 5)
    # # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # cimg = img

    # img = cv2.imread("Frames\\frame.jpg", 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.imshow('mask',mask)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 500, param1=150, param2=30, minRadius=20, maxRadius=500)
    # try:
    circles = np.uint16(np.around(circles))
    # except AttributeError:
    #     circles = 0

    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imshow('detected circles', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
