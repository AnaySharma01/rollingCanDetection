#Imports necessary packages
import cv2 as cv
import numpy as np

#Creates a mask around the frame
def crop_image(image, vertices):
    #Defines the mask using numpy
    mask = np.zeros_like(image)
    #Fills the mask
    mask_color = 255
    cv.fillPoly(mask, vertices, mask_color)
    masked_image = cv.bitwise_and(image, mask)
    #Returns the mask when called
    return masked_image
