import cv2
import numpy as np


bigger_picture = cv2.imread("C:\\Users\\Batu\\Desktop\\gulresmi.jpg",cv2.IMREAD_COLOR) # will be used for printing the other images
sea_img = cv2.imread("C:\\Users\\Batu\\Desktop\\plajresmi.jpg", cv2.IMREAD_COLOR) # takes the image as a variable
rose_img = cv2.imread("C:\\Users\\Batu\\Desktop\\gulresmi.jpg", cv2.IMREAD_COLOR)# takes the image as a variable

lower_blue = np.array([50,50,50]) # np array for lower blue
upper_blue = np.array([255,255,255]) # np array for upper blue
lower_red = np.array([155,25,0]) # np array for lower red
upper_red = np.array([179,255,255]) # np array for upper red

blue_hsv = cv2.cvtColor(sea_img,cv2.COLOR_BGR2HSV) #makes the image HSV
red_hsv = cv2.cvtColor(rose_img,cv2.COLOR_BGR2HSV) #makes the imgae HSV

blue_mask = cv2.inRange(blue_hsv,lower_blue,upper_blue) # the filter which will be used for filtering the picture for tones of blue
red_mask = cv2.inRange(red_hsv,lower_red,upper_red) # the filter which will be used for filtering the picture for tones of red

red_results = cv2.bitwise_and(rose_img, rose_img, mask= red_mask)
blue_results = cv2.bitwise_and(sea_img,sea_img, mask = blue_mask) # gets the filtered results

sea_img = blue_results.copy() # copies the filtered version of the image to the old one
rose_img = red_results.copy() #copies the filtered version of the image to the old one

resized_sea_img = cv2.resize(sea_img, (0,0), fx=0.5, fy=1) # decreases x axis value to half 
resized_rose_img = cv2.resize(rose_img, (0,0), fx=0.5, fy=1) # decreases x axis value to half

bigger_picture[:667,:500] = resized_sea_img # sets the left side of the picture as sea_img
bigger_picture[:667,500:] = resized_rose_img # sets the right side of the picture as rose_img

cv2.imshow("results",bigger_picture)
cv2.waitKey(0) 
cv2.destroyAllWindows()
