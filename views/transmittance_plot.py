import numpy as np
from PyQt5.QtWidgets import *
from models.pixel import (get_pixels_by_id,)
from models.plot import (Plot,)

class TransmittancePlot(Plot):
	def __init__(self, parent=None):
		Plot.__init__(self, parent)
		self.ax.set_xlabel('Frequency (THz)')
		self.ax.set_ylabel('Transmittance')
		self.time_vector = None
		self.has_time_vector = False

	def set_time_vector(self, time_0, time_n):
		self.time_vector = np.linspace(time_0, time_n, 
			self.app.thz_img.n_waveforms)
		self.has_time_vector = True

	def plot_transmittances(self, ids):
		self.ax.clear()
		for id in ids:
			px = get_pixels_by_id(self.app, id)
			transmittance, freq = px.thz_pulse.get_transmittance_domain(self.app.length)
			self.ax.semilogy(freq, transmittance, color=px.color, 
				linewidth=1, markersize=2, label=px.name)
		self.ax.set_xlabel('Frequency (THz)')
		self.ax.set_ylabel('Transmittance')
		self.set_plot_options(self.app.t_options)
		self.draw()