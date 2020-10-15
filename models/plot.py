
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class Plot(QWidget):
	def __init__(self, parent=None, toolbar=True):
		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False, figsize=(20, 10), dpi=80,
			facecolor='black', edgecolor='black')
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0.08,0.1,0.91,0.90])
		self.ax = self.canvas.axes
		self.setLayout(vertical_layout)
		# self.ax.clear()
		if toolbar:
			self.toolbar = NavigationToolbar(self.canvas, self)
			self.layout().addWidget(self.toolbar)
	
		self.draw()

	def draw(self):
		self.canvas.draw()
		self.canvas.flush_events()
		# self.canvas.show()

	def set_plot_options(self, options):
		if options['legend']:
			self.ax.legend()
		if options['grid']:
			self.ax.grid(True)
