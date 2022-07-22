import cv2
import numpy as np

# will be used for printing both pictures side by side
bigger_picture = cv2.imread("C:\\Users\\Batu\\Desktop\\gulresmi.jpg",cv2.IMREAD_COLOR) 

# takes the image as a variable
sea_img = cv2.imread("C:\\Users\\Batu\\Desktop\\plajresmi.jpg", cv2.IMREAD_COLOR) 
rose_img = cv2.imread("C:\\Users\\Batu\\Desktop\\gulresmi.jpg", cv2.IMREAD_COLOR)

# np arrays for upper and lower blue & red
lower_blue = np.array([50,50,50]) 
upper_blue = np.array([255,255,255]) 
lower_red = np.array([155,25,0]) 
upper_red = np.array([179,255,255]) 

# makes both images HSV
blue_hsv = cv2.cvtColor(sea_img,cv2.COLOR_BGR2HSV) 
red_hsv = cv2.cvtColor(rose_img,cv2.COLOR_BGR2HSV) 

#the filters which will be used for filtering the pictures for wanted colour tones
blue_mask = cv2.inRange(blue_hsv,lower_blue,upper_blue) 
red_mask = cv2.inRange(red_hsv,lower_red,upper_red) 

#gets the filtered results
red_results = cv2.bitwise_and(rose_img, rose_img, mask= red_mask)
blue_results = cv2.bitwise_and(sea_img,sea_img, mask = blue_mask) 

# changes both old images with the new filtered ones
sea_img = blue_results.copy() 
rose_img = red_results.copy() 

# halves x axis value in both pictures
resized_sea_img = cv2.resize(sea_img, (0,0), fx=0.5, fy=1) 
resized_rose_img = cv2.resize(rose_img, (0,0), fx=0.5, fy=1) 

#adjustes the right places for both pictures(left and right)
bigger_picture[:667,:500] = resized_sea_img 
bigger_picture[:667,500:] = resized_rose_img 

cv2.imshow("results",bigger_picture) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
