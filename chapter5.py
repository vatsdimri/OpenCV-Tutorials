# Warp perspective

import cv2 as cv
import numpy as np

img = cv.imread('resources\cards.webp')
cv.imshow("cards", img)
width, height = 250, 350
points = np.float32([[205,280],[440,260],[683,591],[470,708]])
pts2 = np.float32([[0,0],[width, 0],[width, height],[0, height]])
matrix = cv.getPerspectiveTransform(points, pts2)
imgout = cv.warpPerspective(img, matrix, (width, height))
cv.imshow("output", imgout)

cv.waitKey(0)