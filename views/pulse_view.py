from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
from models.pixel import (get_pixels_by_id,)
from models.plot import (Plot,)

class PulseView(Plot):
	
	def __init__(self, parent = None):
		Plot.__init__(self, parent, toolbar=False)
		self.ax.set_xlabel('Waveform')
		self.ax.set_ylabel('Terahertz Signal')
		self.row = 0
		self.canvas.mpl_connect('button_press_event', self.onclick)
		self.canvas.mpl_connect('motion_notify_event', self.onmove)
		self.canvas.mpl_connect('scroll_event', self.onscroll)

	def onload(self):
		self.max_row = self.app.thz_img.dataset.shape[0]-1

	def refresh(self, data, onload=False):
		if onload:
			self.row = int(len(data)/2)
		self.plot(data)
		self.app._imaging()
		self.set_app_values()

	def onclick(self,event):
		ix = int(event.xdata) if event.xdata is not None else None
		if ix is not None:
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

	def set_cursor(self):
		self.cursor = Cursor(self.ax, 
			useblit=False, color='blue', linewidth=.5, linestyle='--')
		self.cursor.horizOn = False

	def plot_time_point(self, data):
		if self.app.options['time_point']:
			x_points = (self.row, self.row)
			y_points = (min(data), max(data))
			self.ax.plot(x_points, y_points,'r--', lw=.5)
			self.ax.text(
				x_points[0], 
				y_points[1]/2.5, 'Time Point',
				fontsize=6,
				color='red',
				rotation='vertical',
				rotation_mode='anchor')

	def plot(self, data, **kwargs):
		self.ax.clear()
		self.ax.grid(True)
		self.ax.plot(data, 
			color='black', linewidth=0.5, **kwargs)
		self.plot_time_point(data)
		self.ax.set_xlabel('Waveform')
		self.ax.set_ylabel('Terahertz Signal')
		self.set_cursor()
		self.draw()
