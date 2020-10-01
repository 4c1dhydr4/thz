import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

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
		self.pulse = data
		self.plot_pulse()
		self.plot_freq()
		self.plot_trans()
		self.plot_abs()
		self.canvas.draw()

	def plot_pulse(self):
		self.ax1.clear()
		self.ax1.plot(self.pulse, 
			color='red', linewidth=0.5, markersize=12)
		self.ax1.set_xlabel('Optical Delay (ps)')
		self.ax1.set_ylabel('Terahertz Signal')

	def plot_freq(self):
		self.fft = np.abs(np.fft.fft(self.pulse))[0:400]
		self.f = np.linspace(0,4,self.fft.shape[0])
		self.ax2.clear()
		self.ax2.semilogy(self.f, self.fft, 
			color='black', linewidth=0.5, markersize=12)
		self.ax2.set_xlabel('Frequency (THz)')
		self.ax2.set_ylabel('Electric Field (a.u)')

	def plot_trans(self):
		self.T = self.pulse[0:400]/self.fft
		self.ax3.clear()
		self.ax3.semilogy(self.T,
			color='green', linewidth=0.5, markersize=12)
		self.ax3.set_xlabel('Frequency (THz)')
		self.ax3.set_ylabel('Transmitance')

	def plot_abs(self):
		self.ax4.clear()
		self.ax4.plot(self.pulse, 
			color='blue', linewidth=0.5, markersize=12)
		self.ax4.set_xlabel('Frequency (THz)')
		self.ax4.set_ylabel('Absorvance')
