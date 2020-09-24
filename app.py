from PyQt5 import QtCore, QtGui, QtWidgets
from thz import THZImage
from views.load_dialog import *

def load_test(self):
	print('Load Test Img')
	self.thz_img = THZImage('D:\\THz\\Samples\\1.csv')

	self.psSlider.setMaximum(self.thz_img.dataset.shape[0]-1)
	self.psSlider.setPageStep(1)


	self.img_view.show_img(self.thz_img.get_img(self.psSlider.value()))

def sliders(self):
	ps = self.psSlider.value()
	self.img_view.show_img(self.thz_img.get_img(ps))
	# self.img_view.show_img(self.thz_img.get_img(ps), interpolation='blackman', cmap='hot')
	self.pulse_view.plot(self.thz_img.get_column(0))

def set_main_definitions(self):
	# Setear funciones a controles de interfaz con cada objeto (botones, sliders, etc.)
	self.testButton.clicked.connect(self._load_test)
	self.psSlider.valueChanged.connect(self._sliders)

def main__name__(Ui_MainWindow):
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	# ui._load_test()
	MainWindow.show()
	sys.exit(app.exec_())