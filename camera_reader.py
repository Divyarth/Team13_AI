# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:06:31 2017

@author: HP
"""


    
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from boss_train import Model
from image_show import App


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    cap = cv2.VideoCapture(0)
    cascade_path = 'C:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml'
    model = Model()
   
    model.load()
    while True:
        _, frame = cap.read()

        
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        cascade = cv2.CascadeClassifier(cascade_path)

        
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  
            for rect in facerect:
                

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                result = model.predict(image)
                if result == 0:  # boss
                    print('Boss is approaching')
                    ex.show_image()
                else:
                    print('Not boss')

        
        k = cv2.waitKey(100)
        if k == 27:
            break

    
    cap.release()
    cv2.destroyAllWindows()
