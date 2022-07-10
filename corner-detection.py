import cv2
import numpy as np


img = cv2.imread("C:\\Users\\Batu\\Desktop\\chess-board.png",cv2.IMREAD_GRAYSCALE) #black-white version of the image

corners = cv2.goodFeaturesToTrack(img, 100, 0.5, 10) #finding corners
corners = np.int0(corners) # changing np ints to normal ints

for corner in corners:
    x,y = corner.ravel() # getting the coordinates of corners
    cv2.circle(img, (x,y), 5, (255,0,0), -1) # drawing a circle on each corner


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()