# Shapes and texts
import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv.imshow('black image', img)

# for color functionality 
img2 = np.ones((512, 512, 3), np.uint8)
img2[:] = 255, 255, 0 # Here the order of the colors is blue, green, red
# cv.imshow('IMG2 image ', img2)

# If we want the color in only a certain part of the image 
img2[100:200, 100:200] = 255, 0, 0

# Creating lines in opencv
cv.line(img, (0,0), (300,300), (0,255,0), 1)
cv.imshow("Chapter 4 shapes, lines and text", img)

cv.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 1)
cv.imshow("Chapter 4 shapes, lines and text", img)

# Creating a rectangle in opencv
cv.rectangle(img, (0,0), (200,300), (0,0,255), 2)
cv.imshow("Chapter 4 shapes, lines and text", img)

# Creating filled (solid) rectangle in opencv We use cv.FILLED
cv.rectangle(img, (0,0), (200,300), (0,0,255), cv.FILLED)
cv.imshow("Chapter 4 shapes, lines and text", img)

# Creating a circle in opencv
cv.circle(img, (200,200), 100, (255,0,0),2)
cv.imshow("Chapter 4 shapes, lines and text", img)

# Adding text to the image
cv.putText(img, 'open cv', (300, 100), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
cv.imshow("Chapter 4 shapes, lines and text", img)




cv.waitKey(0)
        
    




