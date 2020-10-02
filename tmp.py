# pyuic5 ui/main.ui>tmp.py
from PyQt5 import QtCore, QtGui, QtWidgets
from views.img_view import ImgView
from views.pulse_view import PulseView
from views.plots_view import PlotsView
from app import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_view = ImgView(self.centralwidget)
        self.img_view.setGeometry(QtCore.QRect(-1, 0, 511, 611))
        self.img_view.setObjectName("img_view")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, -10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(510, 20, 831, 621))
        self.tab.setObjectName("tab")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 201, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.view_mode_cb = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.view_mode_cb.setObjectName("view_mode_cb")
        self.verticalLayout_2.addWidget(self.view_mode_cb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.sample_info_text = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.sample_info_text.setObjectName("sample_info_text")
        self.verticalLayout_2.addWidget(self.sample_info_text)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(270, 350, 151, 22))
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 350, 151, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cursor_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.cursor_label.setObjectName("cursor_label")
        self.horizontalLayout_3.addWidget(self.cursor_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 350, 131, 22))
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
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 370, 181, 149))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.interpolation_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.interpolation_cb.setObjectName("interpolation_cb")
        self.verticalLayout.addWidget(self.interpolation_cb)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cmaptype_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmaptype_cb.setObjectName("cmaptype_cb")
        self.verticalLayout.addWidget(self.cmaptype_cb)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.cmap_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cmap_cb.setObjectName("cmap_cb")
        self.verticalLayout.addWidget(self.cmap_cb)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_1)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 350, 101, 22))
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
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.pulse_view = PulseView(self.tab_1)
        self.pulse_view.setGeometry(QtCore.QRect(0, 0, 821, 341))
        self.pulse_view.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pulse_view.setObjectName("pulse_view")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 370, 151, 130))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.time_point_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.time_point_checkbox.setObjectName("time_point_checkbox")
        self.verticalLayout_3.addWidget(self.time_point_checkbox)
        self.axes_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.axes_checkbox.setObjectName("axes_checkbox")
        self.verticalLayout_3.addWidget(self.axes_checkbox)
        self.point_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.point_checkbox.setObjectName("point_checkbox")
        self.verticalLayout_3.addWidget(self.point_checkbox)
        self.multiple_points_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.multiple_points_checkbox.setObjectName("multiple_points_checkbox")
        self.verticalLayout_3.addWidget(self.multiple_points_checkbox)
        self.transparent_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.transparent_checkbox.setObjectName("transparent_checkbox")
        self.verticalLayout_3.addWidget(self.transparent_checkbox)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 530, 340, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.load_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout_5.addWidget(self.load_button)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_5.addWidget(self.save_button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.export_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout_5.addWidget(self.export_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(570, 350, 251, 241))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.pixels_tree = QtWidgets.QTreeWidget(self.verticalLayoutWidget_5)
        self.pixels_tree.setObjectName("pixels_tree")
        self.verticalLayout_5.addWidget(self.pixels_tree)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_pixel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.add_pixel_button.setObjectName("add_pixel_button")
        self.horizontalLayout_6.addWidget(self.add_pixel_button)
        self.remove_pixel_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.remove_pixel_button.setObjectName("remove_pixel_button")
        self.horizontalLayout_6.addWidget(self.remove_pixel_button)
        self.change_color_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.change_color_button.setObjectName("change_color_button")
        self.horizontalLayout_6.addWidget(self.change_color_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.plot_pixels_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.plot_pixels_button.setObjectName("plot_pixels_button")
        self.horizontalLayout_8.addWidget(self.plot_pixels_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.tab.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plots_view = PlotsView(self.tab_2)
        self.plots_view.setGeometry(QtCore.QRect(0, 0, 821, 481))
        self.plots_view.setObjectName("plots_view")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 490, 251, 61))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.export_plots_button = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.export_plots_button.setObjectName("export_plots_button")
        self.horizontalLayout_7.addWidget(self.export_plots_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(290, 490, 101, 80))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.grid_checkbox.setObjectName("grid_checkbox")
        self.verticalLayout_7.addWidget(self.grid_checkbox)
        self.tab.addTab(self.tab_2, "")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 610, 160, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.zoom_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.zoom_button.setObjectName("zoom_button")
        self.horizontalLayout_9.addWidget(self.zoom_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        set_main_definitions(self, MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "THz Imaging Software"))
        self.label_3.setText(_translate("MainWindow", "Terahertz Pulse Imaging and Analysis Software"))
        self.label_5.setText(_translate("MainWindow", "Image View Mode:"))
        self.label_6.setText(_translate("MainWindow", "Sample Information:"))
        self.signal_label.setText(_translate("MainWindow", "Signal Value:"))
        self.cursor_label.setText(_translate("MainWindow", "Cursor Point:"))
        self.index_label.setText(_translate("MainWindow", "Pixel Index:"))
        self.label.setText(_translate("MainWindow", "Interpolation:"))
        self.label_2.setText(_translate("MainWindow", "Color Map Type:"))
        self.label_4.setText(_translate("MainWindow", "Color Map:"))
        self.waveform_point_label.setText(_translate("MainWindow", "Time Point:"))
        self.label_7.setText(_translate("MainWindow", "Tools Options:"))
        self.time_point_checkbox.setText(_translate("MainWindow", "Show Time Point Line"))
        self.axes_checkbox.setText(_translate("MainWindow", "Show Image Axes Cursor"))
        self.point_checkbox.setText(_translate("MainWindow", "Show Actual Pixel"))
        self.multiple_points_checkbox.setText(_translate("MainWindow", "Show Multiple Pixels"))
        self.transparent_checkbox.setText(_translate("MainWindow", "Transparent Points"))
        self.label_8.setText(_translate("MainWindow", "Options:"))
        self.load_button.setText(_translate("MainWindow", "Load Sample"))
        self.save_button.setText(_translate("MainWindow", "Save Project"))
        self.export_button.setText(_translate("MainWindow", "Export Data"))
        self.label_9.setText(_translate("MainWindow", "Selected Pixels:"))
        self.pixels_tree.headerItem().setText(0, _translate("MainWindow", "Name/Index"))
        self.pixels_tree.headerItem().setText(1, _translate("MainWindow", "Color"))
        self.pixels_tree.headerItem().setText(2, _translate("MainWindow", "ID"))
        self.add_pixel_button.setText(_translate("MainWindow", "Add"))
        self.remove_pixel_button.setText(_translate("MainWindow", "Remove"))
        self.change_color_button.setText(_translate("MainWindow", "Change Color"))
        self.plot_pixels_button.setText(_translate("MainWindow", "Plot Pixels"))
        self.tab.setTabText(self.tab.indexOf(self.tab_1), _translate("MainWindow", "Imaging"))
        self.label_10.setText(_translate("MainWindow", "Plots Tools:"))
        self.export_plots_button.setText(_translate("MainWindow", "Export Plots"))
        self.label_11.setText(_translate("MainWindow", "Plots Options:"))
        self.grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("MainWindow", "Plots"))
        self.zoom_button.setText(_translate("MainWindow", "Zoom"))

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

    def _set_options(self, state):
        set_options(self, state)

    def _add_pixel_to_list(self):
        add_pixel_to_list(self)

    def _remove_pixel_to_list(self):
        remove_pixel_to_list(self)

    def _change_color_pixel_list(self):
        change_color_pixel_list(self)

if __name__ == "__main__":
    main__name__(Ui_MainWindow)