import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from models.pixel import (get_pixels_by_id,)

class PulsePlot(QWidget):
	
	def __init__(self, parent = None):

		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False, figsize=(20, 10), dpi=80,
			facecolor='black', edgecolor='black')
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0.08,0.1,0.91,0.90])
		self.ax = self.canvas.axes
		self.setLayout(vertical_layout)
		self.ax.clear()
		self.ax.set_xlabel('Optical Delay (ps)')
		self.ax.set_ylabel('Terahertz Signal')
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.layout().addWidget(self.toolbar)
		self.canvas.draw()
		self.time_vector = None
		self.has_time_vector = False

	def set_time_vector(self, time_0, time_n):
		self.time_vector = np.linspace(time_0, time_n, self.app.thz_img.n_waveforms)
		self.has_time_vector = True
	def draw(self):
		self.canvas.draw()
		self.canvas.show()

	def plot_pulses(self, ids):
		self.ax.clear()
		if self.app.pp_options['grid']:
			self.ax.grid(True)
		for id in ids:
			px = get_pixels_by_id(self.app, id)
			if self.has_time_vector:
				self.ax.plot(self.time_vector, px.thz_pulse.data,color=px.color, 
					linewidth=1, markersize=2, label=px.name)
				if self.app.pp_options['reference']:
					self.ax.plot(self.time_vector, self.app.thz_img.reference,color='k', 
						linewidth=.8, markersize=2, label='Reference Pulse')
				self.ax.set_xlabel('Optical Delay (ps)')
			else:
				self.ax.plot(px.thz_pulse.data,color=px.color, 
					linewidth=1, markersize=2, label=px.name)
				if self.app.pp_options['reference']:
					self.ax.plot(self.app.thz_img.reference,color='k', 
						linewidth=.8, markersize=2, label='Reference Pulse')
				self.ax.set_xlabel('Waveform')
		if self.app.pp_options['legend']:
			self.ax.legend()
		self.ax.set_ylabel('Terahertz Signal')
		self.draw()