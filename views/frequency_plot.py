import numpy as np
from PyQt5.QtWidgets import *
from models.pixel import (get_pixels_by_id,)
from models.plot import (Plot,)

class FrequencyPlot(Plot):
	def __init__(self, parent=None):
		Plot.__init__(self, parent)
		self.ax.set_xlabel('Frequency (THz)')
		self.ax.set_ylabel('Terahertz Signal')
		self.time_vector = None
		self.has_time_vector = False

	def set_time_vector(self, time_0, time_n):
		self.time_vector = np.linspace(time_0, time_n, 
			self.app.thz_img.n_waveforms)
		self.has_time_vector = True

	def plot_freq(self, ids):
		self.ax.clear()
		for id in ids:
			px = get_pixels_by_id(self.app, id)
			fft, freq = px.thz_pulse.get_frequency_domain(self.app.length)
			self.ax.semilogy(freq, fft, color=px.color, 
				linewidth=1, markersize=2, label=px.name)
			self.ax.set_xlabel('Frequency (THz)')
		
		if self.app.fd_options['reference']:
			self.ax.plot(freq, px.thz_pulse.fft_ref[:self.app.length], color='k', 
				linewidth=.8, markersize=2, label='Reference Pulse')

		self.ax.set_ylabel('Terahertz Signal')
		self.set_plot_options(self.app.fd_options)
		self.draw()