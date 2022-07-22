import cv2
import numpy

# takes the video feed
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read() # reads the image coming from camera
    frame = cv2.flip(frame,1) # reversing mirror effect
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # making the frame gray

    #cascades which will be used for detection of face and eyes
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2) #rectangle around face
        roi_gray = gray_frame[y:y+h, x:x+w] #face in gray colour
        roi_color = frame[y:y+h, x:x+w] # coloured face

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2) #rectangle around eyes

    cv2.imshow("frame",frame)

    #break if user presses 'q'
    if(cv2.waitKey(1) == ord('q')):
        break 

cap.release()
cv2.destroyAllWindows()
