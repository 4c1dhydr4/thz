import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from thz import (Pulse,)

class PlotsView(QWidget):
	
	def __init__(self, parent = None):

		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False, figsize=(20, 10), dpi=60,
			facecolor='black', edgecolor='black')
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.ax1 = self.fig.add_subplot(221)
		self.canvas.ax2 = self.fig.add_subplot(222)
		self.canvas.ax3 = self.fig.add_subplot(223)
		self.canvas.ax4 = self.fig.add_subplot(224)
		self.ax1 = self.canvas.ax1
		self.ax2 = self.canvas.ax2
		self.ax3 = self.canvas.ax3
		self.ax4 = self.canvas.ax4
		self.setLayout(vertical_layout)
		# self.ax.clear()
		self.canvas.draw()

	def onload(self):
		pass

	def refresh(self, data):
		self.pulse = Pulse(data, self.app.thz_img.reference)
		self.plot_pulse()
		self.plot_freq()
		self.plot_trans()
		self.plot_abs()
		self.canvas.draw()
		self.canvas.flush_events()

	def plot_pulse(self):
		self.ax1.clear()
		if self.app.options['grid']:
			self.ax1.grid(True)
		self.ax1.plot(self.pulse.data, 
			color='red', linewidth=0.5, markersize=12)
		self.ax1.set_xlabel('Optical Delay (ps)')
		self.ax1.set_ylabel('Terahertz Signal')

	def plot_freq(self):
		fft, freq = self.pulse.get_frequency_domain(self.app.length)
		self.ax2.clear()
		if self.app.options['grid']:
			self.ax2.grid(True)
		self.ax2.semilogy(freq, fft, 
			color='black', linewidth=0.5, markersize=12)
		self.ax2.set_xlabel('Frequency (THz)')
		self.ax2.set_ylabel('Electric Field (a.u)')

	def plot_trans(self):
		transmittance, freq = self.pulse.get_transmittance_domain(self.app.length)
		self.ax3.clear()
		if self.app.options['grid']:
			self.ax3.grid(True)
		self.ax3.semilogy(freq, transmittance,
			color='green', linewidth=0.5, markersize=12)
		self.ax3.set_xlabel('Frequency (THz)')
		self.ax3.set_ylabel('Transmitance')

	def plot_abs(self):
		absorbance, freq = self.pulse.get_absorbance(self.app.length)
		self.ax4.clear()
		if self.app.options['grid']:
			self.ax4.grid(True)
		self.ax4.semilogy(freq, absorbance,
			color='blue', linewidth=0.5, markersize=12)
		self.ax4.set_xlabel('Frequency (THz)')
		self.ax4.set_ylabel('Absorbance')
