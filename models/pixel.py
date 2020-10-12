from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTreeWidgetItem
from components.tools import (show_message, get_rand_color)
from thz import (Pulse,)

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
		self.is_checked = True
		self.thz_pulse = Pulse(self.pulse)

	def change_color(self):
		self.color = get_rand_color()

	def set_checked(self):
		self.is_checked = True

	def set_unchecked(self):
		self.is_checked = False


def set_all_unchecked(self):
	for pixel in self.pixel_list:
		pixel.set_unchecked()

def selected_pixels_tree(self):
	set_all_unchecked(self)
	pixel_ids = []
	for index in range(self.pixels_tree.topLevelItemCount()):
		item = self.pixels_tree.topLevelItem(index)
		if item.checkState(0) == 2:
			id = int(item.text(2))
			pixel_ids.append(id)
			pixel = get_pixels_by_id(self,id)
			pixel.set_checked()
	return pixel_ids

def get_pixels_by_id(self, id):
	for item in self.pixel_list:
		if item.id == id:
			return item 
	return None

def refresh_pixels_tree(self):
	self.pixels_tree.clear()
	for pixel in self.pixel_list:
		R = QTreeWidgetItem(
			self.pixels_tree,[
				str('{}: [{}, {}]'.format(pixel.name, pixel.ix, pixel.iy)), 
				None,
				str(pixel.id)])
		if pixel.is_checked:
			R.setCheckState(0, 2)
		else:
			R.setCheckState(0, 0)
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
