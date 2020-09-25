from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.path import Path
# from matplotlib import patches as patches

plt.rcParams["figure.figsize"] = (20,10)

class PulseView(QWidget):
	
	def __init__(self, parent = None):

		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False)
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0.125,0.11,0.85,0.85])
		self.canvas.axes.grid(True)
		self.setLayout(vertical_layout)
		self.canvas.axes.clear()
		self.canvas.draw()
		self.cli = self.canvas.mpl_connect('button_press_event', self.onclick)
		self.max = 0
		self.row = 0

	def onclick(self,event):
		ix = int(event.xdata)
		if ix >= 0 and ix <= self.max:
			self.row = ix
			self.plot(self.data)
			self.imaging()

	def draw(self):
		self.canvas.draw()
		self.canvas.show()

	def set_cursor(self):
		self.cursor = Cursor(self.canvas.axes, 
			useblit=False, color='blue', linewidth=1, linestyle='--')
		self.cursor.horizOn = False

	def plot(self, data, **kwargs):
		self.data = data
		self.canvas.axes.clear()
		self.canvas.axes.plot(self.data, **kwargs)
		self.canvas.axes.plot([self.row,self.row], [0,max(self.data)], 'r-.', lw=.5)
		self.set_cursor()
		self.draw()