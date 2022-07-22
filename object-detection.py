import cv2
import numpy as np

# original and black&white version of the football practice image
img = cv2.imread("C:\\Users\\Batu\\Desktop\\football-practice.jpeg",cv2.IMREAD_GRAYSCALE) # black&white football practice image
img2 = cv2.imread("C:\\Users\\Batu\\Desktop\\football-practice.jpeg",cv2.IMREAD_COLOR) # orginial football practice image

# images of the shoe and the ball
shoe_template = cv2.imread("C:\\Users\\Batu\\Desktop\\shoe-template.png",cv2.IMREAD_GRAYSCALE) 
ball_template = cv2.imread("C:\\Users\\Batu\\Desktop\\ball-template.png",cv2.IMREAD_GRAYSCALE) 

Methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] # methods for finding objects

# getting the sizes of shoe and ball template
sh,sw = shoe_template.shape 
bh,bw = ball_template.shape 


for method in Methods: #for using all methods
    #searchs and gets the coordinates of the shoe
    shoe_result = cv2.matchTemplate(img,shoe_template,method) # searchs shoe 
    s_min_val,s_max_val,s_min_loc,s_max_loc = cv2.minMaxLoc(shoe_result) # gets the coordinates of the shoe
    
    #searchs and gets the coordinates of the ball
    ball_result = cv2.matchTemplate(img,ball_template,method)
    b_min_val,b_max_val,b_min_loc,b_max_loc = cv2.minMaxLoc(ball_result) 

    # takes the right coordinates 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: 
        s_location = s_min_loc
        b_location = b_min_loc
    else: 
        s_location = s_max_loc
        b_location = b_max_loc

    # finds bottom right corner of a rectangle around the shoe and the ball, then draws it
    s_bottom_right = (s_location[0] + sw, s_location[1] + sh) 
    b_bottom_right = (b_location[0] + bw, b_location[1] + bh) 

    # draws the rectangles
    cv2.rectangle(img2, s_location, s_bottom_right, (255,0,0), 2) 
    cv2.rectangle(img2, b_location, b_bottom_right, (0,255,0), 2) 

    cv2.imshow("img", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

