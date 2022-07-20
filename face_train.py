import cv2 
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

people = ["Ben Affleck", "Madonna", "Benedict Cumberbatch"]
features = []
labels = []

DIR = r"C:\\Users\\User\\Documents\\VSCode\\People"
def create_train(features,labels):
    
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            current_face =cv2.imread(img_path)
            gray = cv2.cvtColor(current_face, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1 , 5)

            for (x,y,w,h) in faces:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

    
create_train(features,labels)

print(f"Length of the features = {len(features)}")
print(f"Length of the labels = {len(labels)}")

features = np.array(features, dtype=object)
labels = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save("training.yml")


print("Done--------------")


        