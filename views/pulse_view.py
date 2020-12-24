import numpy as np
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
		self.time_vector = None
		self.has_time_vector = False
		self.row = 0
		self.ix = 0.0
		self.canvas.mpl_connect('button_press_event', self.onclick)
		self.canvas.mpl_connect('motion_notify_event', self.onmove)
		self.canvas.mpl_connect('scroll_event', self.onscroll)

	def onload(self):
		self.max_row = self.app.thz_img.dataset.shape[0]-1

	def set_time_vector(self, time_0, time_n):
		self.time_vector = np.linspace(time_0, time_n, 
			self.app.thz_img.n_waveforms)
		self.has_time_vector = True

	def refresh(self, data, onload=False):
		if onload:
			self.row = int(len(data)/2)
		self.plot(data)
		self.app._imaging()
		self.set_app_values()

	def onclick(self,event):
		if self.has_time_vector:
			self.ix = float(event.xdata) if event.xdata is not None else None
		else:
			self.ix = int(event.xdata) if event.xdata is not None else None
		if self.ix is not None:
			if self.has_time_vector:
				if self.ix >= min(self.time_vector) and self.ix <= max(self.time_vector):
					self.row = self.search_row(self.ix)
			else:
				if self.ix >= 0 and self.ix <= self.max_row:
					self.row = self.ix
			self.refresh(self.app.pulse)

	def search_row(self, ix):
		index = 0
		for i in self.time_vector:
			if ix < i:
				return index
			index += 1

	def search_ix(self, row, data):
		index = 0
		for i in data:
			if row == i:
				return self.time_vector[row]
			index += 1

	def set_time_point_by_row(self, row, data):
		self.row = row
		self.ix = self.search_ix(row,data)
		self.plot_time_point(data, text=False)
		self.draw()

	def onmove(self, event):
		if not event.inaxes:
			return
		x, y = event.xdata, event.ydata
		self.app.cursor_label.setText('Cursor Point: [%.1f,%.1f]'%(x,y))

	def onscroll(self, event):
		if event.button == 'up':
			self.row += 1
			if self.has_time_vector:
				self.ix += .1
		elif event.button == 'down':
			self.row -= 1
			if self.has_time_vector:
				self.ix -= .1

		if self.row < 0:
			self.row = 0
			if self.has_time_vector:
				self.ix += min(self.time_vector)
		elif self.row > self.max_row:
			self.row = self.max_row
			if self.has_time_vector:
				self.ix += max(self.time_vector)

		self.refresh(self.app.pulse)

	def set_app_values(self):
		self.app.waveform_point_label.setText('Time Point: {}'.format(self.row))
		self.app.signal_label.setText('Signal Value: {}'.format(self.app.pulse[self.row]))

	def set_cursor(self):
		self.cursor = Cursor(self.ax, 
			useblit=False, color='blue', linewidth=.5, linestyle='--')
		self.cursor.horizOn = False

	def plot_time_point(self, data, text=True):
		if self.app.options['time_point']:
			x_points = (self.ix, self.ix)
			y_points = (min(data), max(data))
			self.ax.plot(x_points, y_points,'r--', lw=.5)
			if text:
				self.ax.text(
					x_points[0], 
					y_points[1]/2.5, 'Time Point',
					fontsize=6,
					color='red',
					rotation='vertical',
					rotation_mode='anchor')


	def plot(self, data, **kwargs):
		self.ax.clear()
		if self.app.options['grid']:
			self.ax.grid(True)
		if self.has_time_vector:
			self.ax.plot(self.time_vector, data, color='black', linewidth=0.5, **kwargs)
			self.ax.set_xlabel('Optical Delay (ps)')
		else:
			self.ax.plot(data, color='black', linewidth=0.5, **kwargs)
			self.ax.set_xlabel('Waveform')
		self.plot_time_point(data)
		self.ax.set_ylabel('Terahertz Signal')
		self.set_cursor()
		self.draw()
