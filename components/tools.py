import random
from PyQt5.QtWidgets import QMessageBox


def show_message(icon='warning', title="Mensaje", text="Texto", info="Extra Info"):
	if icon == 'info':
		icn = QMessageBox.Information
	elif icon == 'danger':
		icn = QMessageBox.Critical
	elif icon == 'warning':
		icn = QMessageBox.Warning
	else:
		icn = QMessageBox.Question
	msg = QMessageBox()
	msg.setIcon(icn)
	msg.setWindowTitle(title)
	msg.setText(text)
	msg.setInformativeText(info)
	msg.setStandardButtons(QMessageBox.Ok)
	ok = msg.exec_()

def get_rand_color():
	return "#{:06x}".format(random.randint(0, 0xFFFFFF))