# This tutorial is about Resizing and Cropping images
import cv2 as cv
import numpy as np

# first we need to understand the how coordinates work on images

# In mathematics 
# positive x  start from left to right 
# positive y  start from bottom to top

# In image processing
# positive x starts from left to right 
# positive y starts from top to bottom

# Reading Images
img = cv.imread('resources\Image1.jpg')

# Resizing the Image
(w, h) = img.shape[:2]
w_new = 1000                    # this is the x axis of the image
h_new = w_new * h//w            # this is the y axis of the image
dim = (w_new, h_new)
img = cv.resize(img, dim)
cv.imshow('Output', img)

# Cropping the image
# To keep in mind that the order in which we crop is opposite of the order in which we Resize
# During resizing we used (width, height)
# For cropping we have to use [height_range, width_range]
imcropped = img[0:200, 100:500]
cv.imshow('Cropped', imcropped)


cv.waitKey(0)