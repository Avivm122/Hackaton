import cv2

cap = cv2.VideoCapture(0)
ret, First_frame = cap.read()
First_frame_gray = cv2.cvtColor(First_frame, cv2.COLOR_BGR2GRAY)

while(cap.isOpened()):
    _, current_frame = cap.read()
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    frame_diff = cv2.absdiff(current_frame_gray, First_frame_gray)

    cv2.imshow('frame diff ', frame_diff)
    print("New frame:")
    print(frame_diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()