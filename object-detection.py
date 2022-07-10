import cv2
import numpy as np


img = cv2.imread("C:\\Users\\Batu\\Desktop\\football-practice.jpeg",cv2.IMREAD_GRAYSCALE) # black&white football practice image
img2 = cv2.imread("C:\\Users\\Batu\\Desktop\\football-practice.jpeg",cv2.IMREAD_COLOR) # orginial football practice image
shoe_template = cv2.imread("C:\\Users\\Batu\\Desktop\\shoe-template.png",cv2.IMREAD_GRAYSCALE) # image of the black&white shoe
ball_template = cv2.imread("C:\\Users\\Batu\\Desktop\\ball-template.png",cv2.IMREAD_GRAYSCALE) # image of the black&white ball

Methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] # methods for finding objects

sh,sw = shoe_template.shape # getting size of shoe-template
bh,bw = ball_template.shape # getting size of ball-template


for method in Methods: #for using all methodsd
    shoe_result = cv2.matchTemplate(img,shoe_template,method) # searchs shoe 
    s_min_val,s_max_val,s_min_loc,s_max_loc = cv2.minMaxLoc(shoe_result) # gets the coordinates of the shoe
    
    ball_result = cv2.matchTemplate(img,ball_template,method) # searchs ball
    b_min_val,b_max_val,b_min_loc,b_max_loc = cv2.minMaxLoc(ball_result) # gets the coordinates of the ball

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: # making sure locations are being got correctly
        s_location = s_min_loc
        b_location = b_min_loc
    
    else: # making sure locations are being got correctly
        s_location = s_max_loc
        b_location = b_max_loc

    s_bottom_right = (s_location[0] + sw, s_location[1] + sh) # finding bottom right corner of a rectangle around shoe for drawing it
    b_bottom_right = (b_location[0] + bw, b_location[1] + bh) # finding bottom right corner of a rectangle around ball for drawing it

    cv2.rectangle(img2, s_location, s_bottom_right, (255,0,0), 2) # draws the rectangle
    cv2.rectangle(img2, b_location, b_bottom_right, (0,255,0), 2) # draws the rectangle

    cv2.imshow("img", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

