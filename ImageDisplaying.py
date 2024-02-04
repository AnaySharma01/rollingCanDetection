#Imports necessary packages
import cv2 as cv

def displayImage(masked_image):
    #Returns the processed image
    cv.imshow("circleWithDetection", masked_image)
    cv.waitKey(1)
