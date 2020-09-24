from PyQt5 import QtCore, QtGui, QtWidgets
from views.img_view import *
from views.pulse_view import *
from app import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_view = ImgView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(10, 0, 500, 521))
        self.img_view.setObjectName("img_view")
        self.psSlider = QtWidgets.QSlider(self.centralwidget)
        self.psSlider.setGeometry(QtCore.QRect(10, 520, 501, 22))
        self.psSlider.setOrientation(QtCore.Qt.Horizontal)
        self.psSlider.setObjectName("psSlider")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(220, 560, 111, 23))
        self.testButton.setObjectName("testButton")
        self.pulse_view = PulseView(self.centralwidget)
        self.pulse_view.setGeometry(QtCore.QRect(520, 0, 491, 211))
        self.pulse_view.setObjectName("pulse_view")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))

    def _load_test(self):
        load_test(self)

    def _sliders(self):
        sliders(self)

if __name__ == "__main__":
    main__name__(Ui_MainWindow)