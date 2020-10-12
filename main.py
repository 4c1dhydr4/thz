from PyQt5 import QtWidgets
from window import Ui_MainWindow

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui._set_main_definitions(MainWindow)
	ui._load_test()
	MainWindow.show()
	sys.exit(app.exec_())