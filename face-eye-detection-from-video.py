import cv2


cap = cv2.VideoCapture("C:\\Users\\Batu\\Desktop\\video.mp4") # gets the video

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # the object which will be used for detecting the face
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml") # the object which will be used for detecting eyes

while True:
    ret,frame = cap.read() #gets the frame in the video
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # makes the frame gray 
    
    faces = face_cascade.detectMultiScale(gray_frame,1.3,3) # finds the face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1) # drawing a rectangle around the face with green
        roi_gray = gray_frame[y: y+h, x: x+w] # getting face's axises in black-white image
        roi_color = frame[y: y+h, x: x+w] # getting faces' axises in original image

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.5, 4) # detecting location of eyes in every frame of video
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255), 1) #draws e rectangle around every eye

    cv2.imshow("frame",frame)

    if cv2.waitKey(60) == ord('q'): # quits if user presses q letter
        break

    continue

cap.release() # releases the source for further usages
cv2.destroyAllWindows()