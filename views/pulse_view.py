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
		self.canvas.axes = self.fig.add_axes([0.08,0.15,0.90,0.80])
		self.canvas.axes.grid(True)
		self.setLayout(vertical_layout)
		self.canvas.axes.clear()
		self.canvas.axes.set_xlabel('Optical Delay (ps)')
		self.canvas.axes.set_ylabel('Terahertz Signal')
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
			useblit=False, color='blue', linewidth=.5, linestyle='--')
		self.cursor.horizOn = False

	def plot(self, data, **kwargs):
		self.data = data
		self.canvas.axes.clear()
		self.canvas.axes.plot(self.data, 
			color='green', linewidth=0.5, markersize=12, **kwargs)
		self.canvas.axes.plot(
			[self.row,self.row], 
			[min(self.data),max(self.data)], 
			'r--', lw=.5)
		self.canvas.axes.set_xlabel('Optical Delay (ps)')
		self.canvas.axes.set_ylabel('Terahertz Signal')
		self.set_cursor()
		self.draw()