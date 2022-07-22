import cv2
import numpy as np

#black-white version of the image
img = cv2.imread("C:\\Users\\Batu\\Desktop\\chess-board.png",cv2.IMREAD_GRAYSCALE) 

#finding corners
corners = cv2.goodFeaturesToTrack(img, 100, 0.5, 10) 

# changing np ints to normal ints
corners = np.int0(corners) 

# gets the coordinates of corners and draws a circle on each one of them
for corner in corners:
    x,y = corner.ravel() 
    cv2.circle(img, (x,y), 5, (255,0,0), -1) 


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
