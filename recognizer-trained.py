import cv2 
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

people = ["Ben Affleck", "Madonna", "Benedict Cumberbatch"]

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("C:\\Users\\User\\Documents\\VSCode\\Python\\training.yml")

img = cv2.imread("C:\\Users\\User\\Documents\\VSCode\\People\\New Pics\\madonna12.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in face:
    face_roi = gray[y:y+h, x:x+w]

    label,confidence = face_recognizer.predict(face_roi)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv2.putText(img, str(people[label]), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("person",img)
cv2.waitKey(0)
cv2.destroyAllWindows()