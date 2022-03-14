import cv2 as cv


# this like is used to caputre video from the webcam 
# for more than one webcam then the argument of funciton VideoCapture will be the id of the webcam
# eg. cv.VideoCapture(1)  for web cam id 1 
# cv.VideoCapture(webcam_id)
vid = cv.VideoCapture(0) 
vid.set(0, 640) # this set the width of the window of horizontal resolution (id = 0 for horizontal)
vid.set(1, 480) # this is for vertical resolution (id = 1 for vertical)

# changing the brightness of the video
vid.set(10, 50)  # id = 10 for brightness

while True:
    success, img = vid.read()

    cv.imshow("video", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
