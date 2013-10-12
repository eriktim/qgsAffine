# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sat Oct 12 16:42:08 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ui(object):
    def setupUi(self, ui):
        ui.setObjectName(_fromUtf8("ui"))
        ui.resize(337, 255)
        self.labelLayer = QtGui.QLabel(ui)
        self.labelLayer.setGeometry(QtCore.QRect(10, 10, 56, 18))
        self.labelLayer.setObjectName(_fromUtf8("labelLayer"))
        self.comboBoxLayer = QtGui.QComboBox(ui)
        self.comboBoxLayer.setGeometry(QtCore.QRect(90, 10, 241, 23))
        self.comboBoxLayer.setObjectName(_fromUtf8("comboBoxLayer"))
        self.groupBoxParameters = QtGui.QGroupBox(ui)
        self.groupBoxParameters.setGeometry(QtCore.QRect(10, 100, 321, 111))
        self.groupBoxParameters.setObjectName(_fromUtf8("groupBoxParameters"))
        self.lineEditTx = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditTx.setGeometry(QtCore.QRect(90, 80, 61, 24))
        self.lineEditTx.setObjectName(_fromUtf8("lineEditTx"))
        self.lineEditC = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditC.setGeometry(QtCore.QRect(90, 50, 61, 24))
        self.lineEditC.setObjectName(_fromUtf8("lineEditC"))
        self.labelB = QtGui.QLabel(self.groupBoxParameters)
        self.labelB.setGeometry(QtCore.QRect(170, 60, 61, 20))
        self.labelB.setObjectName(_fromUtf8("labelB"))
        self.labelD = QtGui.QLabel(self.groupBoxParameters)
        self.labelD.setGeometry(QtCore.QRect(170, 30, 51, 20))
        self.labelD.setObjectName(_fromUtf8("labelD"))
        self.labelTx = QtGui.QLabel(self.groupBoxParameters)
        self.labelTx.setGeometry(QtCore.QRect(10, 90, 72, 20))
        self.labelTx.setObjectName(_fromUtf8("labelTx"))
        self.labelC = QtGui.QLabel(self.groupBoxParameters)
        self.labelC.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.labelC.setObjectName(_fromUtf8("labelC"))
        self.labelA = QtGui.QLabel(self.groupBoxParameters)
        self.labelA.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.labelA.setObjectName(_fromUtf8("labelA"))
        self.labelTy = QtGui.QLabel(self.groupBoxParameters)
        self.labelTy.setGeometry(QtCore.QRect(170, 90, 72, 20))
        self.labelTy.setObjectName(_fromUtf8("labelTy"))
        self.lineEditA = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditA.setGeometry(QtCore.QRect(90, 20, 61, 24))
        self.lineEditA.setObjectName(_fromUtf8("lineEditA"))
        self.lineEditD = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditD.setGeometry(QtCore.QRect(250, 20, 61, 24))
        self.lineEditD.setObjectName(_fromUtf8("lineEditD"))
        self.lineEditTy = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditTy.setGeometry(QtCore.QRect(250, 80, 61, 24))
        self.lineEditTy.setObjectName(_fromUtf8("lineEditTy"))
        self.lineEditB = QtGui.QLineEdit(self.groupBoxParameters)
        self.lineEditB.setGeometry(QtCore.QRect(250, 50, 61, 24))
        self.lineEditB.setObjectName(_fromUtf8("lineEditB"))
        self.radioButtonSelectedFeatures = QtGui.QRadioButton(ui)
        self.radioButtonSelectedFeatures.setGeometry(QtCore.QRect(10, 40, 141, 24))
        self.radioButtonSelectedFeatures.setChecked(True)
        self.radioButtonSelectedFeatures.setObjectName(_fromUtf8("radioButtonSelectedFeatures"))
        self.radioButtonWholeLayer = QtGui.QRadioButton(ui)
        self.radioButtonWholeLayer.setGeometry(QtCore.QRect(10, 60, 141, 24))
        self.radioButtonWholeLayer.setChecked(False)
        self.radioButtonWholeLayer.setObjectName(_fromUtf8("radioButtonWholeLayer"))
        self.pushButtonRun = QtGui.QPushButton(ui)
        self.pushButtonRun.setGeometry(QtCore.QRect(90, 220, 75, 28))
        self.pushButtonRun.setObjectName(_fromUtf8("pushButtonRun"))
        self.pushButtonInvert = QtGui.QPushButton(ui)
        self.pushButtonInvert.setGeometry(QtCore.QRect(170, 220, 75, 28))
        self.pushButtonInvert.setObjectName(_fromUtf8("pushButtonInvert"))

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)
        ui.setTabOrder(self.comboBoxLayer, self.radioButtonSelectedFeatures)
        ui.setTabOrder(self.radioButtonSelectedFeatures, self.radioButtonWholeLayer)
        ui.setTabOrder(self.radioButtonWholeLayer, self.lineEditA)
        ui.setTabOrder(self.lineEditA, self.lineEditC)
        ui.setTabOrder(self.lineEditC, self.lineEditTx)
        ui.setTabOrder(self.lineEditTx, self.lineEditD)
        ui.setTabOrder(self.lineEditD, self.lineEditB)
        ui.setTabOrder(self.lineEditB, self.lineEditTy)

    def retranslateUi(self, ui):
        ui.setWindowTitle(QtGui.QApplication.translate("ui", "Vector Affine Transformation", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLayer.setText(QtGui.QApplication.translate("ui", "Layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxParameters.setTitle(QtGui.QApplication.translate("ui", "Affine Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTx.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditC.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelB.setText(QtGui.QApplication.translate("ui", "Rotation Y", None, QtGui.QApplication.UnicodeUTF8))
        self.labelD.setText(QtGui.QApplication.translate("ui", "Scale Y", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTx.setText(QtGui.QApplication.translate("ui", "Translation X", None, QtGui.QApplication.UnicodeUTF8))
        self.labelC.setText(QtGui.QApplication.translate("ui", "Rotation X", None, QtGui.QApplication.UnicodeUTF8))
        self.labelA.setText(QtGui.QApplication.translate("ui", "Scale X", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTy.setText(QtGui.QApplication.translate("ui", "Translation Y", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditA.setText(QtGui.QApplication.translate("ui", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditD.setText(QtGui.QApplication.translate("ui", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditTy.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditB.setText(QtGui.QApplication.translate("ui", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonSelectedFeatures.setText(QtGui.QApplication.translate("ui", "Selected Features:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonWholeLayer.setText(QtGui.QApplication.translate("ui", "Whole layer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRun.setText(QtGui.QApplication.translate("ui", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInvert.setText(QtGui.QApplication.translate("ui", "Invert", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = QtGui.QDialog()
    ui = Ui_ui()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())

