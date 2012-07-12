# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Tue Dec  2 21:44:12 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ui(object):
    def setupUi(self, ui):
        ui.setObjectName("ui")
        ui.resize(QtCore.QSize(QtCore.QRect(0,0,337,255).size()).expandedTo(ui.minimumSizeHint()))

        self.label = QtGui.QLabel(ui)
        self.label.setGeometry(QtCore.QRect(10,10,56,18))
        self.label.setObjectName("label")

        self.comboBox = QtGui.QComboBox(ui)
        self.comboBox.setGeometry(QtCore.QRect(90,10,241,23))
        self.comboBox.setObjectName("comboBox")

        self.groupBox = QtGui.QGroupBox(ui)
        self.groupBox.setGeometry(QtCore.QRect(10,100,321,111))
        self.groupBox.setObjectName("groupBox")

        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(90,80,61,24))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(90,50,61,24))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170,60,61,20))
        self.label_7.setObjectName("label_7")

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170,30,51,20))
        self.label_5.setObjectName("label_5")

        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10,90,72,20))
        self.label_8.setObjectName("label_8")

        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10,60,61,20))
        self.label_6.setObjectName("label_6")

        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10,30,51,20))
        self.label_4.setObjectName("label_4")

        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(170,90,72,20))
        self.label_9.setObjectName("label_9")

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90,20,61,24))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(250,20,61,24))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(250,80,61,24))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(250,50,61,24))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.radioButton = QtGui.QRadioButton(ui)
        self.radioButton.setGeometry(QtCore.QRect(10,40,141,24))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtGui.QRadioButton(ui)
        self.radioButton_2.setGeometry(QtCore.QRect(10,60,141,24))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtGui.QPushButton(ui)
        self.pushButton.setGeometry(QtCore.QRect(90,220,75,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(ui)
        self.pushButton_2.setGeometry(QtCore.QRect(170,220,75,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)
        ui.setTabOrder(self.comboBox,self.radioButton)
        ui.setTabOrder(self.radioButton,self.radioButton_2)
        ui.setTabOrder(self.radioButton_2,self.lineEdit)
        ui.setTabOrder(self.lineEdit,self.lineEdit_3)
        ui.setTabOrder(self.lineEdit_3,self.lineEdit_5)
        ui.setTabOrder(self.lineEdit_5,self.lineEdit_2)
        ui.setTabOrder(self.lineEdit_2,self.lineEdit_4)
        ui.setTabOrder(self.lineEdit_4,self.lineEdit_6)

    def retranslateUi(self, ui):
        ui.setWindowTitle(QtGui.QApplication.translate("ui", "Vector Affine Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ui", "Layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ui", "Affine Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ui", "Rotation Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ui", "Scale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ui", "Translation X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ui", "Rotation X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ui", "Scale X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ui", "Translation Y", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("ui", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("ui", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("ui", "Selected Features:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("ui", "Whole layer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ui", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ui", "Undo", None, QtGui.QApplication.UnicodeUTF8))

