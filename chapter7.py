# color detection of images
# Steps taken
# Creating the trackbars to detect the object colors by manually tunning the trackbar
# Using the manual tunning values of Hue, Saturation, and Value parameter 
# We create a mask that will be used to get the object from the image
# Then we use bitwise_and operation to apply the mask
import cv2 as cv
import numpy as np
from chapter6 import stackImages 

# Creating a a slide bar in which we can change the value of the variable during runtime
# The function below will be called when we change the value of the variable
# So we can use the value of the variable to adjust some parameters of image using this function
def empty(i):
    pass
cv.namedWindow("Trackbars")  # Create a window named trackbar
cv.resizeWindow('Trackbars', 640, 300) # resizing he window
cv.createTrackbar("Hue Min", 'Trackbars', 0, 179, empty) 
cv.createTrackbar("Hue Max", 'Trackbars', 179, 179, empty) 
cv.createTrackbar("Sat Min", 'Trackbars', 0, 255, empty) 
cv.createTrackbar("Sat Max", 'Trackbars', 255, 255, empty) 
cv.createTrackbar("Val Min", 'Trackbars', 0, 255, empty) 
cv.createTrackbar("Val Max", 'Trackbars', 255, 255, empty) 

while True:
    img = cv.imread('Resources/Lenna.png')
    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # cv.getTrackbarpos function finds the position of trackbars 
    h_min = cv.getTrackbarPos('Hue Min', 'Trackbars')  
    h_max = cv.getTrackbarPos('Hue Max', 'Trackbars')
    s_max = cv.getTrackbarPos('Sat Max', 'Trackbars')
    s_min = cv.getTrackbarPos('Sat Min', 'Trackbars')
    v_min = cv.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv.getTrackbarPos('Val Max', 'Trackbars')
    
    # Creating a mask using the values of trackbars
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imghsv, lower, upper)

    # Applying the mask on the image
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # Using the function we created in the last program to show all the images in the same window
    imgStack = stackImages([img, imghsv, mask, imgResult],300, 1)
    cv.imshow("stackImages", imgStack)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
