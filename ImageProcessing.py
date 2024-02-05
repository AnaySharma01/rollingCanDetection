# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies gaussian and median blur
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    median_blur = cv.medianBlur(gray_scale, 5)

    # Creates hough circle around image
    circle = cv.HoughCircles(median_blur, cv.HOUGH_GRADIENT, 2, 1000,
                             param1 = 140, param2 = 10,
                             minRadius = 270, maxRadius = 270)

    #If the circle is detected, display them
    if circle is not None:
        #Creates array of points around the circle using the hough lines
        circle_arr = np.uint16(np.round(circle))
        for point in circle_arr[0, :]:
            # Creates the circle around the image
            cv.circle(image, (point[0], point[1]), point[2], (0, 255, 0), 15)
            # Finds the center point of the circle
            cv.circle(image, (point[0], point[1]), 2, (0, 0, 255), 5)
