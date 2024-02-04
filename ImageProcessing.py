# Imports necessary packages
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

def processImage(masked_image):
    # Applies gaussian blur and canny edge detection on image
    gray = cv.cvtColor(masked_image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    canny_image = cv.Canny(gray_scale, 100, 120)

    # Creates hough lines around image
    circle = cv.HoughCircles(canny_image, cv.HOUGH_GRADIENT, 145, 1000,
                             param1=100, param2=200,
                             minRadius= 150, maxRadius=175)

    #If the circle is detected, display them
    if circle is not None:
        #Creates array of points around the circle using the hough lines
        circle_arr = np.uint16(np.round(circle))

        for point in circle_arr[0, :]:
            # Creates the circle around the image
            cv.circle(masked_image, (point[0], point[1]), point[2], (0, 255, 0), 5)
            # Finds the center point of the circle
            cv.circle(masked_image, (point[0], point[1]), 2, (0, 0, 255), 5)
