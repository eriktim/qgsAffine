# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Sat Feb  1 17:29:48 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

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
        self.groupBoxParameters.setGeometry(QtCore.QRect(10, 90, 321, 111))
        self.groupBoxParameters.setObjectName(_fromUtf8("groupBoxParameters"))
        self.spinA = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinA.setGeometry(QtCore.QRect(40, 30, 62, 33))
        self.spinA.setMinimum(-999999.0)
        self.spinA.setMaximum(999999.0)
        self.spinA.setSingleStep(0.1)
        self.spinA.setProperty("value", 1.0)
        self.spinA.setObjectName(_fromUtf8("spinA"))
        self.spinD = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinD.setGeometry(QtCore.QRect(140, 70, 62, 33))
        self.spinD.setMinimum(-999999.0)
        self.spinD.setMaximum(999999.0)
        self.spinD.setSingleStep(0.1)
        self.spinD.setProperty("value", 1.0)
        self.spinD.setObjectName(_fromUtf8("spinD"))
        self.spinC = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinC.setGeometry(QtCore.QRect(40, 70, 62, 33))
        self.spinC.setMinimum(-999999.0)
        self.spinC.setMaximum(999999.0)
        self.spinC.setSingleStep(0.1)
        self.spinC.setProperty("value", 0.0)
        self.spinC.setObjectName(_fromUtf8("spinC"))
        self.spinB = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinB.setGeometry(QtCore.QRect(140, 30, 62, 33))
        self.spinB.setMinimum(-999999.0)
        self.spinB.setMaximum(999999.0)
        self.spinB.setSingleStep(0.1)
        self.spinB.setProperty("value", 0.0)
        self.spinB.setObjectName(_fromUtf8("spinB"))
        self.spinTx = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinTx.setGeometry(QtCore.QRect(240, 30, 62, 33))
        self.spinTx.setMinimum(-999999.0)
        self.spinTx.setMaximum(999999.0)
        self.spinTx.setSingleStep(1.0)
        self.spinTx.setProperty("value", 0.0)
        self.spinTx.setObjectName(_fromUtf8("spinTx"))
        self.spinTy = QtGui.QDoubleSpinBox(self.groupBoxParameters)
        self.spinTy.setGeometry(QtCore.QRect(240, 70, 62, 33))
        self.spinTy.setMinimum(-999999.0)
        self.spinTy.setMaximum(999999.0)
        self.spinTy.setSingleStep(1.0)
        self.spinTy.setProperty("value", 0.0)
        self.spinTy.setObjectName(_fromUtf8("spinTy"))
        self.lblXNew = QtGui.QLabel(self.groupBoxParameters)
        self.lblXNew.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.lblXNew.setObjectName(_fromUtf8("lblXNew"))
        self.lblXPlusX = QtGui.QLabel(self.groupBoxParameters)
        self.lblXPlusX.setGeometry(QtCore.QRect(110, 30, 31, 31))
        self.lblXPlusX.setObjectName(_fromUtf8("lblXPlusX"))
        self.lblYPlusX = QtGui.QLabel(self.groupBoxParameters)
        self.lblYPlusX.setGeometry(QtCore.QRect(210, 30, 31, 31))
        self.lblYPlusX.setObjectName(_fromUtf8("lblYPlusX"))
        self.lblYNew = QtGui.QLabel(self.groupBoxParameters)
        self.lblYNew.setGeometry(QtCore.QRect(10, 70, 31, 31))
        self.lblYNew.setObjectName(_fromUtf8("lblYNew"))
        self.lblXPlusY = QtGui.QLabel(self.groupBoxParameters)
        self.lblXPlusY.setGeometry(QtCore.QRect(110, 70, 31, 31))
        self.lblXPlusY.setObjectName(_fromUtf8("lblXPlusY"))
        self.lblYPlusY = QtGui.QLabel(self.groupBoxParameters)
        self.lblYPlusY.setGeometry(QtCore.QRect(210, 70, 31, 31))
        self.lblYPlusY.setObjectName(_fromUtf8("lblYPlusY"))
        self.radioButtonSelectedFeatures = QtGui.QRadioButton(ui)
        self.radioButtonSelectedFeatures.setGeometry(QtCore.QRect(10, 40, 171, 24))
        self.radioButtonSelectedFeatures.setChecked(True)
        self.radioButtonSelectedFeatures.setObjectName(_fromUtf8("radioButtonSelectedFeatures"))
        self.radioButtonWholeLayer = QtGui.QRadioButton(ui)
        self.radioButtonWholeLayer.setGeometry(QtCore.QRect(10, 60, 141, 24))
        self.radioButtonWholeLayer.setChecked(False)
        self.radioButtonWholeLayer.setObjectName(_fromUtf8("radioButtonWholeLayer"))
        self.pushButtonRun = QtGui.QPushButton(ui)
        self.pushButtonRun.setGeometry(QtCore.QRect(10, 220, 75, 28))
        self.pushButtonRun.setObjectName(_fromUtf8("pushButtonRun"))
        self.pushButtonClose = QtGui.QPushButton(ui)
        self.pushButtonClose.setGeometry(QtCore.QRect(250, 220, 75, 28))
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.pushButtonInvert = QtGui.QPushButton(ui)
        self.pushButtonInvert.setGeometry(QtCore.QRect(90, 220, 101, 28))
        self.pushButtonInvert.setObjectName(_fromUtf8("pushButtonInvert"))

        self.retranslateUi(ui)
        QtCore.QMetaObject.connectSlotsByName(ui)
        ui.setTabOrder(self.comboBoxLayer, self.radioButtonSelectedFeatures)
        ui.setTabOrder(self.radioButtonSelectedFeatures, self.radioButtonWholeLayer)

    def retranslateUi(self, ui):
        ui.setWindowTitle(_translate("ui", "Vector Affine Transformation", None))
        self.labelLayer.setText(_translate("ui", "Layer:", None))
        self.groupBoxParameters.setTitle(_translate("ui", "Transformation Matrix", None))
        self.lblXNew.setText(_translate("ui", "x\' =", None))
        self.lblXPlusX.setText(_translate("ui", "x +", None))
        self.lblYPlusX.setText(_translate("ui", "y +", None))
        self.lblYNew.setText(_translate("ui", "y\' =", None))
        self.lblXPlusY.setText(_translate("ui", "x +", None))
        self.lblYPlusY.setText(_translate("ui", "y +", None))
        self.radioButtonSelectedFeatures.setText(_translate("ui", "Selected features", None))
        self.radioButtonWholeLayer.setText(_translate("ui", "Whole layer", None))
        self.pushButtonRun.setText(_translate("ui", "Transform", None))
        self.pushButtonClose.setText(_translate("ui", "Close", None))
        self.pushButtonInvert.setText(_translate("ui", "Invert Matrix", None))

