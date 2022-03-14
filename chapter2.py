import cv2 as cv
import numpy as np

# Reading Images
img = cv.imread('resources\Lenna.png')


# converting image to grayscale
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', imgray)


# adding the gaussian blur to the image
imblur = cv.GaussianBlur(imgray, (21,21), 0)  # (7,7) is the kernel size of the blur window
# as we increase the kernel size of the window the blur increases
# kernel size can only be odd positive integer 
cv.imshow('blur image', imblur)

# Edge detector canny edge detector
imcanny1 = cv.Canny(img, 200, 200)
cv.imshow('canny edge detector', imcanny1)

# To increase the width of the detected edges we use dilate to apply a filter 
kernel = np.ones((3,3), np.uint8)
imdilation = cv.dilate(imcanny1, kernel, iterations=1)
cv.imshow('dilated image', imdilation)

# Opposite of dilation is erosion it will make the edges thinner
imerode = cv.erode(imdilation, kernel, iterations=1)
cv.imshow('eroded image', imerode)

cv.waitKey(0)