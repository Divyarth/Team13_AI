# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:33:45 2017

@author: HP
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):

    def __init__(self):
        
        super().__init__()
        
 
    def show_image(self):
        self.setWindowTitle('')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('show.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.showFullScreen()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show_image()
    sys.exit(app.exec_())