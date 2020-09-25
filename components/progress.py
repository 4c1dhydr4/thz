from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressDialog


def set_progress(message):
	progress = QProgressDialog()
	progress.setFixedSize(300, 60)
	progress.setAutoFillBackground(True)
	progress.setWindowModality(Qt.WindowModal)
	progress.setWindowTitle('Please wait')
	progress.setLabelText(message)
	progress.setSizeGripEnabled(False)
	progress.setModal(True)
	progress.setCancelButton(None)
	progress.setMinimumDuration(0)
	progress.setAutoClose(False)
	progress.show()
	progress.setValue(1)
	return progress
