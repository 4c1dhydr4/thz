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
		self.canvas.axes = self.fig.add_axes([0.11,0.15,0.90,0.80])
		self.ax = self.canvas.axes
		self.ax.grid(True)
		self.setLayout(vertical_layout)
		self.ax.clear()
		self.ax.set_xlabel('Optical Delay (ps)')
		self.ax.set_ylabel('Terahertz Signal')
		self.row = 0
		self.canvas.draw()
		self.canvas.mpl_connect('button_press_event', self.onclick)
		self.canvas.mpl_connect('motion_notify_event', self.onmove)
		self.canvas.mpl_connect('scroll_event', self.onscroll)

	def onload(self):
		self.max_row = self.app.thz_img.dataset.shape[0]-1

	def refresh(self, data):
		self.plot(data)
		self.app._imaging()
		self.set_app_values()

	def onclick(self,event):
		ix = int(event.xdata)
		if ix >= 0 and ix <= self.max_row:
			self.row = ix
			self.refresh(self.app.pulse)

	def onmove(self, event):
		if not event.inaxes:
			return
		x, y = event.xdata, event.ydata
		self.app.cursor_label.setText('Cursor Point: [%.1f,%.1f]'%(x,y))

	def onscroll(self, event):
		if event.button == 'up':
			self.row += 1
		elif event.button == 'down':
			self.row -= 1

		if self.row < 0:
			self.row = 0
		elif self.row > self.max_row:
			self.row = self.max_row

		self.refresh(self.app.pulse)

	def set_app_values(self):
		self.app.waveform_point_label.setText('Time Point: {}'.format(self.row))
		self.app.signal_label.setText('Signal Value: {}'.format(self.app.pulse[self.row]))		

	def draw(self):
		self.canvas.draw()
		self.canvas.show()

	def set_cursor(self):
		self.cursor = Cursor(self.ax, 
			useblit=False, color='blue', linewidth=.5, linestyle='--')
		self.cursor.horizOn = False

	def plot(self, data, **kwargs):
		x_points = (self.row, self.row)
		y_points = (min(data), max(data))
		self.ax.clear()
		self.ax.plot(data, 
			color='green', linewidth=0.5, markersize=12, **kwargs)
		self.ax.plot(
			x_points,
			y_points, 
			'r--', lw=.5)
		self.ax.text(
			x_points[0], 
			y_points[1]/2.5, 'Time Point',
			fontsize=6,
			color='red',
			rotation='vertical',
			rotation_mode='anchor')
		self.ax.set_xlabel('Optical Delay (ps)')
		self.ax.set_ylabel('Terahertz Signal')
		self.set_cursor()
		self.draw()