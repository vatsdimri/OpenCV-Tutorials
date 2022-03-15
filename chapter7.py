# color detection of images
import cv2 as cv
import numpy as np

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
    cv.imshow("Lenna", img)
    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos('Hue Min', 'Trackbars')
    h_max = cv.getTrackbarPos('Hue Max', 'Trackbars')
    s_max = cv.getTrackbarPos('Sat Max', 'Trackbars')
    s_min = cv.getTrackbarPos('Sat Min', 'Trackbars')
    v_min = cv.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv.getTrackbarPos('Val Max', 'Trackbars')
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imghsv, lower, upper)
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    cv.imshow("Original", img)
    cv.imshow("HSV", imghsv)
    cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
