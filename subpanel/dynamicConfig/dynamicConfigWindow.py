from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DynamicConfig(object):
    def setupUi(self, DynamicConfig):
        DynamicConfig.setObjectName(_fromUtf8("DynamicConfig"))
        DynamicConfig.resize(565, 413)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        DynamicConfig.setPalette(palette)
        self.gridLayout = QtGui.QGridLayout(DynamicConfig)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 4, 1, 1)
        self.frame = QtGui.QFrame(DynamicConfig)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.receiverFrame = QtGui.QFrame(self.frame)
        self.receiverFrame.setFrameShape(QtGui.QFrame.Box)
        self.receiverFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.receiverFrame.setObjectName(_fromUtf8("receiverFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.receiverFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sBusRecv = QtGui.QCheckBox(self.receiverFrame)
        self.sBusRecv.setObjectName(_fromUtf8("sBusRecv"))
        self.horizontalLayout.addWidget(self.sBusRecv)
        self.ppmRecv = QtGui.QCheckBox(self.receiverFrame)
        self.ppmRecv.setObjectName(_fromUtf8("ppmRecv"))
        self.horizontalLayout.addWidget(self.ppmRecv)
        self.normalRecv = QtGui.QCheckBox(self.receiverFrame)
        self.normalRecv.setObjectName(_fromUtf8("normalRecv"))
        self.horizontalLayout.addWidget(self.normalRecv)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.channelCount = QtGui.QComboBox(self.receiverFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.channelCount.setPalette(palette)
        self.channelCount.setObjectName(_fromUtf8("channelCount"))
        self.channelCount.addItem(_fromUtf8(""))
        self.channelCount.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.channelCount)
        self.channelCount_2 = QtGui.QLabel(self.receiverFrame)
        self.channelCount_2.setObjectName(_fromUtf8("channelCount_2"))
        self.horizontalLayout.addWidget(self.channelCount_2)
        self.gridLayout_4.addWidget(self.receiverFrame, 2, 0, 1, 2)
        self.receiverTitle = QtGui.QLabel(self.frame)
        self.receiverTitle.setObjectName(_fromUtf8("receiverTitle"))
        self.gridLayout_4.addWidget(self.receiverTitle, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 6, 0, 1, 1)
        self.motorTitle = QtGui.QLabel(self.frame)
        self.motorTitle.setObjectName(_fromUtf8("motorTitle"))
        self.gridLayout_4.addWidget(self.motorTitle, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 6, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        self.motorConfigFrame = QtGui.QFrame(self.frame)
        self.motorConfigFrame.setFrameShape(QtGui.QFrame.Box)
        self.motorConfigFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.motorConfigFrame.setObjectName(_fromUtf8("motorConfigFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.motorConfigFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.triBox = QtGui.QCheckBox(self.motorConfigFrame)
        self.triBox.setObjectName(_fromUtf8("triBox"))
        self.gridLayout_2.addWidget(self.triBox, 0, 0, 1, 1)
        self.quadBox = QtGui.QCheckBox(self.motorConfigFrame)
        self.quadBox.setObjectName(_fromUtf8("quadBox"))
        self.gridLayout_2.addWidget(self.quadBox, 0, 1, 1, 1)
        self.quadPlusBox = QtGui.QCheckBox(self.motorConfigFrame)
        self.quadPlusBox.setObjectName(_fromUtf8("quadPlusBox"))
        self.gridLayout_2.addWidget(self.quadPlusBox, 0, 2, 1, 1)
        self.Y6Box = QtGui.QCheckBox(self.motorConfigFrame)
        self.Y6Box.setObjectName(_fromUtf8("Y6Box"))
        self.gridLayout_2.addWidget(self.Y6Box, 0, 3, 1, 1)
        self.hexaXBox = QtGui.QCheckBox(self.motorConfigFrame)
        self.hexaXBox.setObjectName(_fromUtf8("hexaXBox"))
        self.gridLayout_2.addWidget(self.hexaXBox, 0, 4, 1, 1)
        self.hexaPlusBox = QtGui.QCheckBox(self.motorConfigFrame)
        self.hexaPlusBox.setObjectName(_fromUtf8("hexaPlusBox"))
        self.gridLayout_2.addWidget(self.hexaPlusBox, 0, 5, 1, 1)
        self.slowESC = QtGui.QCheckBox(self.motorConfigFrame)
        self.slowESC.setObjectName(_fromUtf8("slowESC"))
        self.gridLayout_2.addWidget(self.slowESC, 1, 0, 1, 2)
        self.reverseRotation = QtGui.QCheckBox(self.motorConfigFrame)
        self.reverseRotation.setObjectName(_fromUtf8("reverseRotation"))
        self.gridLayout_2.addWidget(self.reverseRotation, 1, 2, 1, 3)
        self.gridLayout_4.addWidget(self.motorConfigFrame, 4, 0, 1, 2)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 3, 3, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 5, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 3, 6, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 0, 2, 1, 3)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 3, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 3, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 2, 1, 3)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 2, 1, 3)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 6, 2, 1, 3)

        self.retranslateUi(DynamicConfig)
        QtCore.QMetaObject.connectSlotsByName(DynamicConfig)

    def retranslateUi(self, DynamicConfig):
        DynamicConfig.setWindowTitle(QtGui.QApplication.translate("DynamicConfig", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sBusRecv.setText(QtGui.QApplication.translate("DynamicConfig", "SBus", None, QtGui.QApplication.UnicodeUTF8))
        self.ppmRecv.setText(QtGui.QApplication.translate("DynamicConfig", "PPM", None, QtGui.QApplication.UnicodeUTF8))
        self.normalRecv.setText(QtGui.QApplication.translate("DynamicConfig", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.channelCount.setItemText(0, QtGui.QApplication.translate("DynamicConfig", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.channelCount.setItemText(1, QtGui.QApplication.translate("DynamicConfig", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.channelCount_2.setText(QtGui.QApplication.translate("DynamicConfig", "Channel Count", None, QtGui.QApplication.UnicodeUTF8))
        self.receiverTitle.setText(QtGui.QApplication.translate("DynamicConfig", "Receiver", None, QtGui.QApplication.UnicodeUTF8))
        self.motorTitle.setText(QtGui.QApplication.translate("DynamicConfig", "Motor Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DynamicConfig", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.triBox.setText(QtGui.QApplication.translate("DynamicConfig", "Tri", None, QtGui.QApplication.UnicodeUTF8))
        self.quadBox.setText(QtGui.QApplication.translate("DynamicConfig", "Quad", None, QtGui.QApplication.UnicodeUTF8))
        self.quadPlusBox.setText(QtGui.QApplication.translate("DynamicConfig", "Quad +", None, QtGui.QApplication.UnicodeUTF8))
        self.Y6Box.setText(QtGui.QApplication.translate("DynamicConfig", "Y6", None, QtGui.QApplication.UnicodeUTF8))
        self.hexaXBox.setText(QtGui.QApplication.translate("DynamicConfig", "Hexa X", None, QtGui.QApplication.UnicodeUTF8))
        self.hexaPlusBox.setText(QtGui.QApplication.translate("DynamicConfig", "Hexa +", None, QtGui.QApplication.UnicodeUTF8))
        self.slowESC.setText(QtGui.QApplication.translate("DynamicConfig", "Slow ESC", None, QtGui.QApplication.UnicodeUTF8))
        self.reverseRotation.setText(QtGui.QApplication.translate("DynamicConfig", "Reverse Motor Rotation", None, QtGui.QApplication.UnicodeUTF8))

#>>>>>>> Changed rcchannelsetup added rccalibration