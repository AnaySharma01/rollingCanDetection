#Imports necessary packages
import cv2 as cv

def displayImage(masked_image):
    #Creates a numpy array for the processed image

    #Returns the processed image
    cv.imshow("circleWithDetection", masked_image)
    cv.waitKey(1)
    cv.destroyAllWindows()
