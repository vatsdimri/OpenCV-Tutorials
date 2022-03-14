import cv2

# loading video

cap = cv2.VideoCapture('resources/test_video.mp4')
# To capture from webcam we use cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    print('sucess: {}'.format(success))
    # Quitting if we press q key after 1 ms of time 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break