from PyQt5 import QtCore, QtGui, QtWidgets
from views.img_view import *
from views.pulse_view import *
from app import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_view = ImgView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(10, 10, 500, 551))
        self.img_view.setObjectName("img_view")
        self.psSlider = QtWidgets.QSlider(self.centralwidget)
        self.psSlider.setGeometry(QtCore.QRect(520, 580, 501, 22))
        self.psSlider.setOrientation(QtCore.Qt.Horizontal)
        self.psSlider.setObjectName("psSlider")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(780, 500, 201, 23))
        self.testButton.setObjectName("testButton")
        self.pulse_view = PulseView(self.centralwidget)
        self.pulse_view.setGeometry(QtCore.QRect(520, 50, 761, 361))
        self.pulse_view.setObjectName("pulse_view")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 420, 201, 149))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.interpolation_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.interpolation_cb.setObjectName("interpolation_cb")
        self.verticalLayout.addWidget(self.interpolation_cb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cmaptype_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmaptype_cb.setObjectName("cmaptype_cb")
        self.verticalLayout.addWidget(self.cmaptype_cb)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.cmap_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmap_cb.setObjectName("cmap_cb")
        self.verticalLayout.addWidget(self.cmap_cb)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1010, 0, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 570, 231, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.select_pixel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.select_pixel_btn.setObjectName("select_pixel_btn")
        self.horizontalLayout_2.addWidget(self.select_pixel_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1293, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        set_main_definitions(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.label.setText(_translate("MainWindow", "Interpolation:"))
        self.label_2.setText(_translate("MainWindow", "Color Map Type:"))
        self.label_4.setText(_translate("MainWindow", "Color Map:"))
        self.label_3.setText(_translate("MainWindow", "THz Imaging Software"))
        self.select_pixel_btn.setText(_translate("MainWindow", "Select Pixel"))

    def _load_test(self):
        load_test(self)

    def _imaging(self):
        imaging(self)

    def _cmaptype(self):
        cmaptype(self)

    def _cmap(self):
        cmap(self)

    def _interpolation(self):
        interpolation(self)

if __name__ == "__main__":
    main__name__(Ui_MainWindow)