from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import LassoSelector, Cursor
# from matplotlib.path import Path
# from matplotlib import patches as patches
# import random

plt.rcParams["figure.figsize"] = (20,10)
plt.rcParams["axes.grid"] = True

class ImgView(QWidget):
	
	def __init__(self, parent=None):

		QWidget.__init__(self, parent)
		self.ix, self.iy = 0, 0
		self.fig = Figure(frameon=False)
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0, 0, 1, 1])
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.setLayout(vertical_layout)
		self.canvas.axes.clear()
		self.canvas.axes.set_axis_off()
		self.canvas.draw()
		self.cli = self.canvas.mpl_connect('button_press_event', self.onclick)
		self.layout().addWidget(self.toolbar)

	def onclick(self,event):
		self.ix, self.iy = int(event.xdata), int(event.ydata)
		self.pulse_view.plot(self.thz_img.get_column_index(self.ix, self.iy))

	def clear_axes(self):
		self.canvas.axes.clear()
		self.canvas.draw()

	def show_img(self, img,**kwargs):
		self.img = img
		self.canvas.axes.clear()
		self.canvas.axes.imshow(self.img, **kwargs)
		self.canvas.axes.set_axis_off()
		self.canvas.draw()
		self.canvas.show()
		self.cursor = Cursor(self.canvas.axes, useblit=False, 
			color='red', linewidth=1, linestyle='--')