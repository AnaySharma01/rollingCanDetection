#Imports necessary packages
import ImageReading
import ImageProcessing
import ImageDisplaying

#Loads the image
file = "rollingCan3.mov"
circle = ImageReading.readImage(file)


#Applies image detection
ImageProcessing.processImage(circle)

#Displays image with hough lines
ImageDisplaying.displayImage(circle)
