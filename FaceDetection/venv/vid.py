import cv2

cap = cv2.VideoCapture(0)

while True:
    ret_val, img = cap.read()

    if ret_val == False:
        break

    cv2.imshow("Cam", img)