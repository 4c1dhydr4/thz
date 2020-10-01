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
