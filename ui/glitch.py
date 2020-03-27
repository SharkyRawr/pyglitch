# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\glitch.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgInput = QtWidgets.QGraphicsView(self.centralwidget)
        self.imgInput.setObjectName("imgInput")
        self.horizontalLayout.addWidget(self.imgInput)
        self.imgOutput = QtWidgets.QGraphicsView(self.centralwidget)
        self.imgOutput.setObjectName("imgOutput")
        self.horizontalLayout.addWidget(self.imgOutput)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.sliderNumGlitch = QtWidgets.QSlider(self.centralwidget)
        self.sliderNumGlitch.setMinimum(1)
        self.sliderNumGlitch.setOrientation(QtCore.Qt.Horizontal)
        self.sliderNumGlitch.setObjectName("sliderNumGlitch")
        self.horizontalLayout_2.addWidget(self.sliderNumGlitch)
        self.txtGlitch = QtWidgets.QLabel(self.centralwidget)
        self.txtGlitch.setObjectName("txtGlitch")
        self.horizontalLayout_2.addWidget(self.txtGlitch)
        self.cmdRndGlitch = QtWidgets.QPushButton(self.centralwidget)
        self.cmdRndGlitch.setObjectName("cmdRndGlitch")
        self.horizontalLayout_2.addWidget(self.cmdRndGlitch)
        self.cmdSave = QtWidgets.QPushButton(self.centralwidget)
        self.cmdSave.setObjectName("cmdSave")
        self.horizontalLayout_2.addWidget(self.cmdSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMake_animation = QtWidgets.QAction(MainWindow)
        self.actionMake_animation.setObjectName("actionMake_animation")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionMake_animation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Glitcher by Sharky.pw"))
        self.txtGlitch.setText(_translate("MainWindow", "1 byte"))
        self.cmdRndGlitch.setText(_translate("MainWindow", "Glitch it!"))
        self.cmdSave.setText(_translate("MainWindow", "Save glitched"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMake_animation.setText(_translate("MainWindow", "Make animation"))

