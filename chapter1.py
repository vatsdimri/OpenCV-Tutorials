import cv2

print('package imported')


## Reading Images, videos and webcam

# Reading Images

img = cv2.imread('resources\Lenna.png')


cv2.imshow('Output', img)
cv2.waitKey(0)