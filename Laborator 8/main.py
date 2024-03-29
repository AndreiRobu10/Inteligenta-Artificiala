import cv2
import keyboard
face_cascade = cv2.CascadeClassifier("C:\Personal\Projects\lab6\justatext.xml")
cap = cv2.VideoCapture(0)

while not keyboard.is_pressed('esc'):
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
#pip3 install tk
cap.release()