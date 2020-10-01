import random
from PyQt5.QtWidgets import QMessageBox


def show_message(icon=QMessageBox.Warning, title="Mensaje", text="Texto", info="Extra Info"):
	msg = QMessageBox()
	msg.setIcon(icon)
	msg.setWindowTitle(title)
	msg.setText(text)
	msg.setInformativeText(info)
	msg.setStandardButtons(QMessageBox.Ok)
	ok = msg.exec_()

def get_rand_color():
	return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def set_checkboxes_options(self):
	if self.time_point_checkbox.isChecked():
		self.options['time_point'] = True
	else:
		self.options['time_point'] = False

	if self.axes_checkbox.isChecked():
		self.options['axes'] = True
	else:
		self.options['axes'] = False

	if self.point_checkbox.isChecked():
		self.options['points'] = True
	else:
		self.options['points'] = False

	if self.multiple_points_checkbox.isChecked():
		self.options['multiple_points'] = True
	else:
		self.options['multiple_points'] = False

	if self.transparent_checkbox.isChecked():
		self.options['transparent'] = True
	else:
		self.options['transparent'] = False