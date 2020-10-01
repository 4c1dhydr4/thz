from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTreeWidgetItem
from components.tools import (show_message, get_rand_color)

class Pixel():
	id = 0
	name = ''
	ix = 0
	iy = 0
	pulse = []
	color = ''

	def __init__(self, name, ix, iy, thz_img, id):
		self.name = name 
		self.ix = ix
		self.iy = iy
		self.color = get_rand_color()
		self.pulse = thz_img.get_column_index(ix, iy)
		self.id = id

def refresh_pixels_tree(self):
	self.pixels_tree.clear()
	for pixel in self.pixel_list:
		R = QTreeWidgetItem(
			self.pixels_tree,[
				str('{}: [{}, {}]'.format(pixel.name, pixel.ix, pixel.iy)), 
				None,
				str(pixel.id)])
		R.setCheckState(0, QtCore.Qt.Checked)
		R.setBackground(1,QtGui.QBrush(QtGui.QColor(pixel.color)))

def verify_pixel_name(name, pixel_list):
	for pixel in pixel_list:
		if name == pixel.name:
			show_message(icon=QMessageBox.Warning, title="Pixel name exists!", 
				text="Is there another Pixel with the same name: {}".format(name), 
				info="Please, save this pixel with different name")
			return False
	return True

def add_pixel(self, name):
	pixel = Pixel(name, self.img_view.ix, self.img_view.iy, self.thz_img, self.pixel_num)
	self.pixel_num += 1
	self.pixel_list.append(pixel)
	refresh_pixels_tree(self)

def save_pixel(self, name):
	if verify_pixel_name(name, self.pixel_list):
		add_pixel(self,name)
		refresh_pixels_tree(self)
