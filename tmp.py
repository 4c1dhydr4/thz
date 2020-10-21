# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.label_3.setGeometry(QtCore.QRect(710, -10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(510, 30, 831, 621))
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
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 370, 151, 153))
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
        self.grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.grid_checkbox.setObjectName("grid_checkbox")
        self.verticalLayout_3.addWidget(self.grid_checkbox)
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
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pulse_plot = PulsePlot(self.tab_3)
        self.pulse_plot.setGeometry(QtCore.QRect(0, 0, 831, 421))
        self.pulse_plot.setObjectName("pulse_plot")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 430, 91, 92))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.time_start_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.time_start_line.setText("")
        self.time_start_line.setObjectName("time_start_line")
        self.verticalLayout_8.addWidget(self.time_start_line)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.time_end_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.time_end_line.setText("")
        self.time_end_line.setObjectName("time_end_line")
        self.verticalLayout_8.addWidget(self.time_end_line)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(110, 430, 160, 84))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.pp_reference_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.pp_reference_checkbox.setObjectName("pp_reference_checkbox")
        self.verticalLayout_9.addWidget(self.pp_reference_checkbox)
        self.pp_legend_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.pp_legend_checkbox.setObjectName("pp_legend_checkbox")
        self.verticalLayout_9.addWidget(self.pp_legend_checkbox)
        self.pp_grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_9)
        self.pp_grid_checkbox.setObjectName("pp_grid_checkbox")
        self.verticalLayout_9.addWidget(self.pp_grid_checkbox)
        self.pp_reload_button = QtWidgets.QPushButton(self.tab_3)
        self.pp_reload_button.setGeometry(QtCore.QRect(10, 560, 261, 23))
        self.pp_reload_button.setObjectName("pp_reload_button")
        self.tab.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frequency_plot = FrequencyPlot(self.tab_4)
        self.frequency_plot.setGeometry(QtCore.QRect(0, 0, 831, 421))
        self.frequency_plot.setObjectName("frequency_plot")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 430, 111, 84))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.fd_reference_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_10)
        self.fd_reference_checkbox.setObjectName("fd_reference_checkbox")
        self.verticalLayout_10.addWidget(self.fd_reference_checkbox)
        self.fd_legend_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_10)
        self.fd_legend_checkbox.setObjectName("fd_legend_checkbox")
        self.verticalLayout_10.addWidget(self.fd_legend_checkbox)
        self.fd_grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_10)
        self.fd_grid_checkbox.setObjectName("fd_grid_checkbox")
        self.verticalLayout_10.addWidget(self.fd_grid_checkbox)
        self.fd_reload_button = QtWidgets.QPushButton(self.tab_4)
        self.fd_reload_button.setGeometry(QtCore.QRect(10, 560, 131, 21))
        self.fd_reload_button.setObjectName("fd_reload_button")
        self.tab.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.transmittance_plot = TransmittancePlot(self.tab_5)
        self.transmittance_plot.setGeometry(QtCore.QRect(0, 0, 831, 421))
        self.transmittance_plot.setObjectName("transmittance_plot")
        self.t_reload_button = QtWidgets.QPushButton(self.tab_5)
        self.t_reload_button.setGeometry(QtCore.QRect(10, 560, 131, 21))
        self.t_reload_button.setObjectName("t_reload_button")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 430, 111, 84))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.t_reference_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.t_reference_checkbox.setObjectName("t_reference_checkbox")
        self.verticalLayout_11.addWidget(self.t_reference_checkbox)
        self.t_legend_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.t_legend_checkbox.setObjectName("t_legend_checkbox")
        self.verticalLayout_11.addWidget(self.t_legend_checkbox)
        self.t_grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_11)
        self.t_grid_checkbox.setObjectName("t_grid_checkbox")
        self.verticalLayout_11.addWidget(self.t_grid_checkbox)
        self.tab.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.absorbance_plot = AbsorbancePlot(self.tab_6)
        self.absorbance_plot.setGeometry(QtCore.QRect(0, 0, 831, 421))
        self.absorbance_plot.setObjectName("absorbance_plot")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab_6)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 430, 111, 84))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.abs_reference_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.abs_reference_checkbox.setObjectName("abs_reference_checkbox")
        self.verticalLayout_7.addWidget(self.abs_reference_checkbox)
        self.abs_legend_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.abs_legend_checkbox.setObjectName("abs_legend_checkbox")
        self.verticalLayout_7.addWidget(self.abs_legend_checkbox)
        self.abs_grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_7)
        self.abs_grid_checkbox.setObjectName("abs_grid_checkbox")
        self.verticalLayout_7.addWidget(self.abs_grid_checkbox)
        self.abs_reload_button = QtWidgets.QPushButton(self.tab_6)
        self.abs_reload_button.setGeometry(QtCore.QRect(10, 560, 131, 23))
        self.abs_reload_button.setObjectName("abs_reload_button")
        self.tab.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plots_view = PlotsView(self.tab_2)
        self.plots_view.setGeometry(QtCore.QRect(0, 0, 821, 481))
        self.plots_view.setObjectName("plots_view")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 490, 131, 91))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.plots_reference_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.plots_reference_checkbox.setObjectName("plots_reference_checkbox")
        self.verticalLayout_6.addWidget(self.plots_reference_checkbox)
        self.plots_legend_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.plots_legend_checkbox.setObjectName("plots_legend_checkbox")
        self.verticalLayout_6.addWidget(self.plots_legend_checkbox)
        self.plots_grid_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.plots_grid_checkbox.setObjectName("plots_grid_checkbox")
        self.verticalLayout_6.addWidget(self.plots_grid_checkbox)
        self.export_plots_button = QtWidgets.QPushButton(self.tab_2)
        self.export_plots_button.setGeometry(QtCore.QRect(270, 490, 111, 23))
        self.export_plots_button.setObjectName("export_plots_button")
        self.tab.addTab(self.tab_2, "")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 610, 160, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.animation_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.animation_button.setObjectName("animation_button")
        self.horizontalLayout_9.addWidget(self.animation_button)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1190, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1220, 30, 121, 16))
        self.label_18.setObjectName("label_18")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.label_8.setText(_translate("MainWindow", "Options:"))
        self.load_button.setText(_translate("MainWindow", "Load Sample"))
        self.save_button.setText(_translate("MainWindow", "Save Project"))
        self.export_button.setText(_translate("MainWindow", "Export Pixels"))
        self.label_9.setText(_translate("MainWindow", "Selected Pixels:"))
        self.pixels_tree.headerItem().setText(0, _translate("MainWindow", "Name/Index"))
        self.pixels_tree.headerItem().setText(1, _translate("MainWindow", "Color"))
        self.pixels_tree.headerItem().setText(2, _translate("MainWindow", "ID"))
        self.add_pixel_button.setText(_translate("MainWindow", "Add"))
        self.remove_pixel_button.setText(_translate("MainWindow", "Remove"))
        self.change_color_button.setText(_translate("MainWindow", "Change Color"))
        self.plot_pixels_button.setText(_translate("MainWindow", "Analyze Pixels"))
        self.tab.setTabText(self.tab.indexOf(self.tab_1), _translate("MainWindow", "Imaging"))
        self.label_12.setText(_translate("MainWindow", "Time Starts:"))
        self.label_13.setText(_translate("MainWindow", "Time Ends:"))
        self.label_14.setText(_translate("MainWindow", "Plot Options:"))
        self.pp_reference_checkbox.setText(_translate("MainWindow", "Show Reference Pulse"))
        self.pp_legend_checkbox.setText(_translate("MainWindow", "Show Legend"))
        self.pp_grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.pp_reload_button.setText(_translate("MainWindow", "Apply Changes"))
        self.tab.setTabText(self.tab.indexOf(self.tab_3), _translate("MainWindow", "Pulse"))
        self.label_15.setText(_translate("MainWindow", "Plot Options:"))
        self.fd_reference_checkbox.setText(_translate("MainWindow", "Show Reference"))
        self.fd_legend_checkbox.setText(_translate("MainWindow", "Show Legend"))
        self.fd_grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.fd_reload_button.setText(_translate("MainWindow", "Apply Changes"))
        self.tab.setTabText(self.tab.indexOf(self.tab_4), _translate("MainWindow", "Frequency Domain"))
        self.t_reload_button.setText(_translate("MainWindow", "Apply Changes"))
        self.label_16.setText(_translate("MainWindow", "Plot Options:"))
        self.t_reference_checkbox.setText(_translate("MainWindow", "Show Reference"))
        self.t_legend_checkbox.setText(_translate("MainWindow", "Show Legend"))
        self.t_grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.tab.setTabText(self.tab.indexOf(self.tab_5), _translate("MainWindow", "Transmittance"))
        self.label_11.setText(_translate("MainWindow", "Plot Options:"))
        self.abs_reference_checkbox.setText(_translate("MainWindow", "Show Reference"))
        self.abs_legend_checkbox.setText(_translate("MainWindow", "Show Legend"))
        self.abs_grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.abs_reload_button.setText(_translate("MainWindow", "Apply Changes"))
        self.tab.setTabText(self.tab.indexOf(self.tab_6), _translate("MainWindow", "Absorbance"))
        self.label_10.setText(_translate("MainWindow", "Plots Options:"))
        self.plots_reference_checkbox.setText(_translate("MainWindow", "Show Reference"))
        self.plots_legend_checkbox.setText(_translate("MainWindow", "Show Legend"))
        self.plots_grid_checkbox.setText(_translate("MainWindow", "Show Grid"))
        self.export_plots_button.setText(_translate("MainWindow", "Export Plots"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("MainWindow", "Plots"))
        self.animation_button.setText(_translate("MainWindow", "Animate"))
        self.label_17.setText(_translate("MainWindow", "Developed by Luis Quiroz"))
        self.label_18.setText(_translate("MainWindow", "quirozburga@gmail.com"))
from absorbanceplot import AbsorbancePlot
from frequencyplot import FrequencyPlot
from imgview import ImgView
from plotsview import PlotsView
from pulseplot import PulsePlot
from pulseview import PulseView
from transmittanceplot import TransmittancePlot
