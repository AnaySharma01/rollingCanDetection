# Imports necessary packages
import cv2 as cv
import numpy as np

def processImage(image):
    # Applies gaussian blur and canny edge detection on image
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_scale = cv.GaussianBlur(gray, (15, 15), 0)
    canny_image = cv.Canny(gray_scale, 100, 100)

    # Creates hough lines around image
    circle = cv.HoughCircles(canny_image, cv.HOUGH_GRADIENT, 8, 5000,
                             param1 = 50, param2 = 45,
                             minRadius = 300, maxRadius = 300)

    #If the circle is detected, display them
    if circle is not None:
        #Creates array of points around the circle using the hough lines
        circle_arr = np.uint16(np.round(circle))
        for point in circle_arr[0, :]:
            # Creates the circle around the image
            cv.circle(image, (point[0] + 5, point[1] - 14), point[2] + 15, (0, 255, 0), 5)
            # Finds the center point of the circle
            cv.circle(image, (point[0] + 5, point[1] - 14), 2, (0, 0, 255), 5)
