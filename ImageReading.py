#Imports necessary packages
import cv2 as cv

#Imports function for reading images
import ImageProcessing
import ImageDisplaying

def readImage(img):
    #Variable needed for displaying the video
    videoIsPlaying = True

    #Starts the video capture
    video = cv.VideoCapture(img)

    #Prevents program from crashing error
    try:
        count = 0
        #While the video is playing, read the frame, process it & display it
        while videoIsPlaying == True:
            videoIsPlaying, frame = video.read()
            ImageProcessing.processImage(frame)
            if count % 5 == 0:
                ImageDisplaying.displayImage(frame)
            count += 1
        cv.destroyAllWindows()

    #Prints message when video is done
    except: print("The video is done.")
    finally: exit()
