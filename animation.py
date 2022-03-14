# Animation of a box moving on screen using open cv
import cv2 as cv
import numpy as np

def add_box(image, position, side=100, color='blue'):
    '''This function adds a square box of any given size to the image'''
    x = position[1]
    y = position[0]
    if color == 'blue':
        image[x:x+side, y:y+side, 0] = 255
    elif color == 'green':
        image[x:x+side, y:y+side, 1] = 255
    elif color == 'red':
        image[x:x+side, y:y+side, 2] = 255
    return image


def animate(img, start_position=np.array([200, 200]), velocity= np.array([2,3]), side = 50):
    # velocity[0] is y velocity and velocity[1] is x velocity
    # side is the length of the squre to animate
    position = start_position
    while True:
        img[:] = 0, 0, 0
        image = add_box(img, position, side=side)
        cv.imshow('Box Animation', image)
        position = position + velocity
        if position[0] + side >= 511:
            velocity[0] = - velocity[0]
        if position[1] + side >= 511:
            velocity[1] = -velocity[1]
        if position[0] <= 0:
            velocity[0] = - velocity[0]
        if position[1] <= 0:
            velocity[1] = -velocity[1]
        # Quitting if we press q key after 1 ms of time 
        if cv.waitKey(10) & 0xFF == ord('q'): 
            break

img = np.zeros((512, 512, 3), np.uint8)

animate(img)

        
    




