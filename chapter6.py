# Joining Images
import cv2 as cv
import numpy as np

def stackImages( imgs, size=500, axis=0):
    '''This function will stack images of any size and type(colored or grayscale)'''
    img_shapes = [img.shape for img in imgs]
    
    
    for i in range(len(imgs)):
        if len(img_shapes[i]) == 2: # it will imply that the image is a grayscale image
            imgs[i] = np.dstack((imgs[i], imgs[i], imgs[i]))
        shape = list(img_shapes[i][:2])
        
        shape[axis -1] = int(size*shape[axis-1]/shape[axis])
        shape[axis] = size         
        dim = tuple(shape)
        imgs[i] = cv.resize(imgs[i], shape)
    if axis == 0:
        return np.vstack(tuple(imgs))
    return np.hstack(tuple(imgs))
    

img = cv.imread('resources\Lenna.png')

# imghor = np.hstack([img, imgray ])
# cv.imshow("horizontal stacking of Images", imghor)
# imgver = np.vstack((img, img))
# cv.imshow("vertical stacking of Images", imgver)


imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
outimg = stackImages([img, imgray, img],500, 1)
cv.imshow("output", outimg)

cv.waitKey(0)