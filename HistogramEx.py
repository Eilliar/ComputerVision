# -*- coding: utf-8 -*-
"""
Histogram Example 01 - OpenCV cv2.calcHist()
Created on Fri Sep 11 14:00:03 2015

@author: Bruno Godoi Eilliar
"""
debug = True
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
plt.ion()

def Histogram(channel, frame):
    canais = {"red":2, "green": 1, "blue": 0}
    return cv2.calcHist([frame],[canais[channel]], mask = None, 
                          histSize = [256], ranges = [0,256])

# Object to capture image, default webcam on Ubuntu is video0
cameraCapture = cv2.VideoCapture(-1)
# Size of the image (automatically)
(w, h) = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
# Windows
cv2.namedWindow("Video")

print "Starting Video Streaming. Press any key to stop."
success, frame = cameraCapture.read()
if debug: print np.shape(frame)

while success and cv2.waitKey(1) == -1:
    success, frame = cameraCapture.read()
    # Calculate Histograms
    r_hist = Histogram("red", frame)
    g_hist = Histogram("green", frame)
    b_hist = Histogram("blue", frame)
    # Plot Histograms
    plt.figure(1)
    plt.clf()
    for x in [(r_hist, 'r'), (g_hist, 'g'), (b_hist, 'b')]:
        plt.plot(x[0], x[1])
    plt.draw()
    cv2.imshow("Video",frame)
    
if debug:
    print "Red: ", np.shape(r_hist)
    
cameraCapture.release()
cv2.destroyAllWindows()