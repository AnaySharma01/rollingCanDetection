# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies median blur and canny edge detection on image
    median_blur = cv.medianBlur(image, 5)
    canny_image = cv.Canny(median_blur, 100, 100)

    # Creates hough lines around image
    circle = cv.HoughCircles(canny_image, cv.HOUGH_GRADIENT, 12, 2000,
                             param1 = 45, param2 = 45,
                             minRadius = 265, maxRadius = 270)

    #If the circle is detected, display them
    if circle is not None:
        #Creates array of points around the circle using the hough lines
        circle_arr = np.uint16(np.round(circle))
        for point in circle_arr[0, :]:
            # Creates the circle around the image
            cv.circle(image, (point[0], point[1]), point[2], (0, 255, 0), 10)
            # Finds the center point of the circle
            cv.circle(image, (point[0], point[1]), 2, (0, 0, 255), 5)
