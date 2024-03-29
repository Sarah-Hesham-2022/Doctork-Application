﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Doctork .ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import tensorflow
import keras
from keras.models import *
from keras.layers import *
from keras.preprocessing import image
import PIL
from keras.models import load_model
import cv2
from numpy import asarray
import numpy as np 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 881, 471))
        self.label.setStyleSheet("background-image: url(:/newPrefix/i1.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.welcom = QtWidgets.QLabel(self.centralwidget)
        self.welcom.setGeometry(QtCore.QRect(0, 0, 881, 91))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.welcom.setFont(font)
        self.welcom.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.welcom.setAlignment(QtCore.Qt.AlignCenter)
        self.welcom.setObjectName("welcom")
        self.imageshow = QtWidgets.QLabel(self.centralwidget)
        self.imageshow.setGeometry(QtCore.QRect(140, 90, 501, 231))
        self.imageshow.setText("")
        self.imageshow.setObjectName("imageshow")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 410, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.uploadbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.button_clicker())
        self.uploadbutton.setGeometry(QtCore.QRect(400, 410, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.uploadbutton.setFont(font)
        self.uploadbutton.setObjectName("uploadbutton")
        self.predictionlabrl = QtWidgets.QLabel(self.centralwidget)
        self.predictionlabrl.setGeometry(QtCore.QRect(0, 460, 881, 101))
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        font.setPointSize(36)
        self.predictionlabrl.setFont(font)
        self.predictionlabrl.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.predictionlabrl.setText("")
        self.predictionlabrl.setAlignment(QtCore.Qt.AlignCenter)
        self.predictionlabrl.setObjectName("predictionlabrl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 420, 161, 41))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 16pt \"Sakkal Majalla\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.corona_model = load_model("C:\\Users\\Sarah Hesham\\OneDrive\\Documents\\Python\\Doctork Application\\Covid19_CNN.h5")
        self.breast_model= load_model("C:\\Users\\Sarah Hesham\\OneDrive\\Documents\\Python\\Doctork Application\\breast_cancer_project_CNN.h5")
        self.brain_model= load_model("C:\\Users\\Sarah Hesham\\OneDrive\\Documents\\Python\\Doctork Application\\BrainTumor_CNN.h5")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcom.setText(_translate("MainWindow", "Welcom At Doctork"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose ٍSpecialty"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Covid19-Pneumonia"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Breast Cancer"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Brain Cancer"))
        self.uploadbutton.setText(_translate("MainWindow", "Upload Your Image"))
        self.label_2.setText(_translate("MainWindow", "Result Will Be Here"))

    # action taken when button is clicked
    def button_clicker(self):
        file_name = QFileDialog.getOpenFileName()
        if file_name[0] != '':
            w = self.imageshow.width()
            h = self.imageshow.height()
            image = QPixmap(file_name[0])
            self.imageshow.setPixmap(image.scaled(w, h))
            self.choosing_model(self.comboBox.currentIndex(), file_name[0])
        return file_name[0]

    def PreProcessCorona(self,Path):
         img =cv2.imread(Path,0)
         img = cv2.resize(img,(100,100),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
         img=np.array(img).astype(np.uint8)
         img=img/255.0
         img=np.expand_dims(img,axis=0)
         return img

    def PredictCorona(self,img):
        y_pred_img=self.corona_model.predict(img)
        max_value=y_pred_img[0].max()
        if(max_value == y_pred_img[0][0]):
           return "Covid Case"
        elif(max_value == y_pred_img[0][1]):
           return "Healthy Chest"
        else:
           return "Pneumonia case"

    def PreProcessBreast(self,Path):
     img =cv2.imread(Path,0)
     img = cv2.resize(img,(640,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
     img=np.array(img).astype(np.uint8)
     img=img/255.0
     img=np.expand_dims(img,axis=0)
     return img

    def PredictBreast(self,img):
       y_pred_img=self.breast_model.predict(img)
       max_value=y_pred_img[0].max()
       if(y_pred_img >=0.5):
         return "Malignant Breast"
       else:
         return "Benign Breast"

    def PreProcessBrain(self,Path):
     img =cv2.imread(Path,0)
     img = cv2.resize(img,(100,100))
     img=np.array(img).astype(np.uint8)
     img=img/255.0
     img=np.expand_dims(img,axis=0)
     return img

    def PredictBrain(self,img):
       y_pred_img=self.brain_model.predict(img)
       if( y_pred_img[0][0] >=0.5):
         return "Malignant Brain" 
       else:
         return "Benign Brain"

    def choosing_model(self, index, file_name):
        if index == 0:
            self.predictionlabrl.setText('Choose a Disease')
        elif index == 1:
            img=self.PreProcessCorona(file_name)
            self.predictionlabrl.setText(self.PredictCorona(img))
        elif index == 2:
            img=self.PreProcessBreast(file_name)
            self.predictionlabrl.setText(self.PredictBreast(img))
        elif index == 3:
            img=self.PreProcessBrain(file_name)
            self.predictionlabrl.setText(self.PredictBrain(img))
        else:
            self.predictionlabrl.setText('Something Went Wrong')


# import qtimg_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

