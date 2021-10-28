import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades  + 'haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./train/third-party/frontalEyes35x16.xml')
nose_cascade = cv2.CascadeClassifier('./train/third-party/Nose18x15.xml')

glasses = cv2.imread('./train/glasses.png')
mustache = cv2.imread('./train/mustache.png')
img_frame  = cv2.imread('./test/Before.png')




####### FOR COMPLETE FACE ########
faces = face_cascade.detectMultiScale(img_frame, 1.3, 5)
for face in faces:
    x, y, w, h = face
    cv2.rectangle(img_frame, (x,y), (x+w, y+h), (0,.255,255), 2)

    

###### FOR EYES REGION ###########
eyes = eye_cascade.detectMultiScale(img_frame, 1.3, 5)
for eye in eyes:
    ex, ey, ew, eh = eye
    cv2.rectangle(img_frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    glasses = cv2.resize(glasses, (ew, eh))

    #assigning glasses width, height and channels using frame.shape
    gw, gh, gc = glasses.shape

    for i in range(0, gw):
        for j in range(0, gh):
            if glasses[i, j][gc] != 0:
                img_frame[ey+i, ex+j] = glasses[i, j]

    

###### FOR NOSE REGION ############
nose = nose_cascade.detectMultiScale(img_frame, 1.3, 5)
for ns in nose:
    nx, ny, nw, nh = ns

    cv2.rectangle(img_frame, (nx, ny), (nx+nw, ny+nh), (0,255,0), 2)




    cv2.imshow('Image Section', img_frame)
    cv2.waitKey(0)

    key_pressed = cv2.waitKey(1) & 0XFF
    if key_pressed == ord('q'):
        break

