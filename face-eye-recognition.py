import cv2
import numpy as np


img = cv2.imread("C:\\Users\\Batu\\Desktop\\smilingpeople.jpg",cv2.IMREAD_COLOR) #original version of the image
gray_img = cv2.imread("C:\\Users\\Batu\\Desktop\\smilingpeople.jpg",cv2.IMREAD_GRAYSCALE) # black&white version of the image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # the object which will be used for detecting faces
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml") # the object which will be used for detecting eyes
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml") # the object which will be used for detecting smiles

faces = face_cascade.detectMultiScale(gray_img, 1.41, 5) # detecting location of faces in image
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1) # drawing a rectangle around each face with green
    roi_gray = gray_img[y: y+h, x: x+w] # getting faces' axises in black-white image
    roi_color = img[y: y+h, x: x+w] # getting faces' axises in original image

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 4) # detecting location of eyes in image
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 1) # drawing a rectangle around each eye with blue

    smiles = smile_cascade.detectMultiScale(roi_gray, 1.27, 6) # detecting location of smiles in image
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0,0,255), 1) # drawing a rectangle around each smile with red


cv2.imshow("img",img) 
cv2.waitKey(0)
cv2.destroyAllWindows()