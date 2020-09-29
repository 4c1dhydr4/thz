# pyuic5 ui/main.ui>tmp.py
from PyQt5 import QtCore, QtGui, QtWidgets
from views.img_view import *
from views.pulse_view import *
from app import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_view = ImgView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(-1, 0, 511, 641))
        self.img_view.setObjectName("img_view")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(740, 590, 201, 23))
        self.testButton.setObjectName("testButton")
        self.pulse_view = PulseView(self.centralwidget)
        self.pulse_view.setGeometry(QtCore.QRect(510, 40, 821, 371))
        self.pulse_view.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pulse_view.setObjectName("pulse_view")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(740, 430, 201, 149))
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
        self.label_3.setGeometry(QtCore.QRect(600, 0, 561, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(940, 410, 131, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.index_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.index_label.setFont(font)
        self.index_label.setObjectName("index_label")
        self.horizontalLayout.addWidget(self.index_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(520, 430, 201, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.view_mode_cb = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.view_mode_cb.setObjectName("view_mode_cb")
        self.verticalLayout_2.addWidget(self.view_mode_cb)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.sample_info_text = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.sample_info_text.setObjectName("sample_info_text")
        self.verticalLayout_2.addWidget(self.sample_info_text)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(670, 410, 101, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.waveform_point_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.waveform_point_label.setFont(font)
        self.waveform_point_label.setObjectName("waveform_point_label")
        self.horizontalLayout_2.addWidget(self.waveform_point_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(520, 410, 151, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cursor_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.cursor_label.setObjectName("cursor_label")
        self.horizontalLayout_3.addWidget(self.cursor_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(780, 410, 151, 22))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.signal_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signal_label.setFont(font)
        self.signal_label.setObjectName("signal_label")
        self.horizontalLayout_4.addWidget(self.signal_label)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        set_main_definitions(self, MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THz Imaging Software"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.label.setText(_translate("MainWindow", "Interpolation:"))
        self.label_2.setText(_translate("MainWindow", "Color Map Type:"))
        self.label_4.setText(_translate("MainWindow", "Color Map:"))
        self.label_3.setText(_translate("MainWindow", "Terahertz Pulse Imaging and Analysis Software"))
        self.index_label.setText(_translate("MainWindow", "Pixel Index:"))
        self.label_5.setText(_translate("MainWindow", "Image View Mode:"))
        self.label_6.setText(_translate("MainWindow", "Sample Information:"))
        self.waveform_point_label.setText(_translate("MainWindow", "Time Point:"))
        self.cursor_label.setText(_translate("MainWindow", "Cursor Point:"))
        self.signal_label.setText(_translate("MainWindow", "Signal Value:"))

    def _refresh(self):
        refresh(self)

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
    
    def _key_press_event(self, event):
        key_press_event(self, event)

if __name__ == "__main__":
    main__name__(Ui_MainWindow)