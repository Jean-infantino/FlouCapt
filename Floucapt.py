#!/usr/python
# -*- coding: utf-8 -*-

"""
------------------------------------------------
Class Floucapt
------------------------------------------------
date: 19/03/2014
------------------------------------------------
version : 1.2
------------------------------------------------

"""

import sys, os
import cv2 as cv
import time
from PIL import Image

class Floucapt:
  
    def faceDetection (image):
        """  Detect the faces on the picture passed in parameter and return the area of faces detected  """

        img = cv.imread(image) # Picture loading in memory

        if not img.data: 
            print ("Erreur d'ouverture de l'image")

        faceModel = cv.CascadeClassifier ("/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml") 
     
        faces = faceModel.detectMultiScale (img, 1.3, 4, cv.cv.CV_HAAR_SCALE_IMAGE, (20,20))   # Face detection

        faces [:, 2:] = faces [:, 2:] + faces [:, :2]

        return faces


    def faceBlurring (faces, image):
        """  Apply a blur on face detected thanks to the first parameter and return the picture blurred  """

        img = cv.imread (image)

        if not img.data: 
            print ("Erreur d'ouverture de l'image")

        for x1, y1, x2, y2 in faces:

            faceDetected = img[y1:y2, x1:x2]
            faceDetected = cv.GaussianBlur(faceDetected,(69,69),0)

            img [y1:y2, x1:x2] = faceDetected

        return img


    def saveImage (img):
        """  Save the picture passed in first parameter under the picture name passed in second parameter """

        date = time.strftime('%Y-%m-%d', time.localtime())
        hourMinSec = time.strftime('%H:%M:%S', time.localtime())

        folder = "img/"

        if not os.path.isdir (folder):
            os.makedirs (folder)

        fileName = date + "-" + hourMinSec + ".jpg"
        save = cv.imwrite (folder + fileName, img)

        fileName = "current.jpg"
        save = cv.imwrite (folder + fileName, img)


    if __name__ == "__main__":

        """  Allowed file formats : png,jpg, jpeg
             Every picture files will be processed (detection and blurring of the faces) abd then saved.
             Files containing 'faces' at the beginning of their names are not processed  """

        for file in os.listdir (".") :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

            if file.startswith ("visage") : continue # déjà traité

            if os.path.splitext(file)[-1].lower() in [".jpg", ".jpeg", ".png" ] :
                faces = faceDetection (file)
                img = faceBlurring (faces, file)
                saveImage (img)
