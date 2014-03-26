#!/usr/python
# -*- coding: utf-8 -*-

"""
------------------------------------------------
Class FlouCapt
------------------------------------------------
authors: Kévin Renévot and Thomas Elain
------------------------------------------------
date: 26/03/2014
------------------------------------------------
version : 1.3
------------------------------------------------

"""

import cv, cv2
import os, time
import numpy
from PIL import Image
import TimeException

class FlouCapt:
  
    def faceDetection (image):
        """  Detect the faces on the picture passed in parameter and return the area of faces detected  """

        # Picture loading in memory
        img = cv2.imread (image) 

        faceModel = cv2.CascadeClassifier ("/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml") 
        faces = faceModel.detectMultiScale (img)

        # Throws an exception if no face is detected on the image
        try:
            faces [:, 2:] = faces [:, 2:] + faces [:, :2]
        except TypeError:
            print ("No face detected")

        return faces


    def faceBlurring (faces, image):
        """  Apply a blur on face detected thanks to the first parameter and return the picture blurred  """

        img = cv2.imread (image)

        for x1, y1, x2, y2 in faces:

            faceDetected = img [y1:y2, x1:x2]
            faceDetected = cv2.GaussianBlur(faceDetected,(69,69),0)

            img [y1:y2, x1:x2] = faceDetected

        return img


    def saveImage (img):
        """  Save the picture passed in first parameter under the picture name passed in second parameter """

        date = time.strftime('%Y-%m-%d', time.localtime())
        hourMinSec = time.strftime('%H:%M:%S', time.localtime())

        folder = "img/" + date + "/"

        # If the folder doesn't exist
        if not os.path.isdir( folder ):
            os.makedirs( folder )

        fileName = date + "-" + hourMinSec + ".jpg"
        cv2.imwrite (folder + fileName, img)
        fileName = "../../current.jpg"
        cv2.imwrite (folder + fileName, img)


    def getImageCapture (videoFlow):
        """  Capture the current image of camera/IP camera video flow and save it in current.jpg file  """

        capture = cv.CaptureFromFile (videoFlow)
        frame = cv.QueryFrame (capture)
        image = cv.SaveImage ("current.jpg", frame)


    if __name__ == "__main__":
        
        while True:
            # The url camera video flow, you may have to modify it according to the IP camera
            video = "http://192.168.0.4:81/snapshot.cgi?user=admin&pwd=&"     
            
            getImageCapture (video)
            faces = faceDetection ("current.jpg")
            img = faceBlurring (faces, "current.jpg")
            saveImage (img)

            # Wait of 30 sec
            time.sleep (30)