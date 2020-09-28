from PyQt5 import (QtCore, QtGui, QtWidgets,)
from thz import (THZImage,)
from components.combos import (fill_interpolation_cb, fill_cmaptype_cb, change_cmap_cb,
	fill_image_view_mode_cb,)
from components.progress import (set_progress,)

def on_load(self):
	self.img_view.app = self
	self.pulse_view.app = self
	self.pulse_view.onload()
	self.sample_info_text.setPlainText(self.thz_img.get_image_details())

def load_test(self):
	self.file_path = 'D:\\THz\\Samples\\Arandano_02.csv'
	self.progress = set_progress('Loading THz Image')
	self.thz_img = THZImage(self.file_path, self.progress)
	self.progress.close()
	on_load(self)
	self.pulse_view.plot(self.thz_img.get_column_index(0,0))
	self._imaging()

def imaging(self):
	if self.thz_img:
		cmap = str(self.cmap_cb.currentText())
		cmap = cmap if cmap != '' else None
		interpolation = str(self.interpolation_cb.currentText())
		self.img_view.show_img(
			self.thz_img.get_img(self.pulse_view.row),
			interpolation=interpolation,
			cmap=cmap)

def cmaptype(self):
	option = str(self.cmaptype_cb.currentText())
	change_cmap_cb(option, self.cmap_cb, self.first_load)

def set_main_definitions(self):
	# Setear funciones a controles de interfaz con cada objeto (botones, sliders, etc.)
	self.first_load = True
	self.thz_img = None
	self.testButton.clicked.connect(self._load_test)
	self.cmaptype_cb.currentTextChanged.connect(self._cmaptype)
	self.cmap_cb.currentTextChanged.connect(self._imaging)
	self.interpolation_cb.currentTextChanged.connect(self._imaging)
	fill_interpolation_cb(self.interpolation_cb)
	fill_cmaptype_cb(self.cmaptype_cb)
	fill_image_view_mode_cb(self.view_mode_cb)
	self.waveform_point_label.setText('Time Point: 0')
	self.index_label.setText('Pixel Index: [0,0]')
	self.sample_info_text.setReadOnly(True)
	self.first_load = False

def main__name__(Ui_MainWindow):
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui._load_test()
	MainWindow.show()
	sys.exit(app.exec_())