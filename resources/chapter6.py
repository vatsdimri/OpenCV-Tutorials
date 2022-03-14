# Joining Images
import cv2 as cv
import numpy as np

img = cv.imread('resources\Lenna.png')
imghor = np.hstack((img, img ))
cv.imshow("horizontal stacking of Images", imghor)

imgver = np.vstack((img, img))
cv.imshow("vertical stacking of Images", imgver)

cv.waitKey(0)