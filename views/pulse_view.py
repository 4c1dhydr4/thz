from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# from matplotlib.widgets import LassoSelector, Cursor
# from matplotlib.path import Path
# from matplotlib import patches as patches
import random

plt.rcParams["figure.figsize"] = (20,10)
plt.rcParams["axes.grid"] = True

class PulseView(QWidget):
	
	def __init__(self, parent = None):

		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False)
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0, 0, 1, 1])
		# self.toolbar = NavigationToolbar(self.canvas, self)
		self.setLayout(vertical_layout)
		self.canvas.axes.clear()
		self.canvas.axes.set_axis_off()
		self.canvas.draw()
		# self.layout().addWidget(self.toolbar)

	def clear(self):
		self.canvas.axes.clear()
		self.canvas.draw()

	def draw(self):
		self.canvas.draw()
		self.canvas.show()

	def plot(self, data, **kwargs):
		self.clear()
		self.canvas.axes.plot(data, **kwargs)
		self.draw()

	def show_img(self, img, **kwargs):
		self.canvas.axes.clear()
		self.canvas.axes.imshow(img, **kwargs)
		self.canvas.axes.set_axis_off()
		self.draw()