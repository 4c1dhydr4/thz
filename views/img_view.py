import time
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import Cursor
import matplotlib.animation as animation
from matplotlib import pyplot as plt
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.path import Path
# from matplotlib import patches as patches
# import random

class ImgView(QWidget):
	
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ix, self.iy = 0, 0
		self.fig = Figure(frameon=False)
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0, 0, 1, 1])
		self.ax = self.canvas.axes
		# self.toolbar = NavigationToolbar(self.canvas, self)
		self.setLayout(vertical_layout)
		self.ax.clear()
		self.ax.set_axis_off()
		self.canvas.draw()
		self.cli = self.canvas.mpl_connect('button_press_event', self.onclick)
		# self.layout().addWidget(self.toolbar)

	def onclick(self,event):
		self.ix, self.iy = int(event.xdata), int(event.ydata)
		self.refresh()

	def refresh(self):
		if self.control_coords():
			self.app.pulse = self.app.thz_img.get_column_index(self.ix, self.iy)
			self.app.pulse_view.plot(self.app.pulse)
			self.app.pulse_view.set_app_values()
			self.app._imaging()
			self.app.plots_view.refresh(self.app.pulse)
			# self.canvas.draw()
			# self.canvas.flush_events()
			self.set_app_values()

	def control_coords(self):
		if self.ix < 0:
			self.ix = 0
			return False
		elif self.ix > self.app.thz_img.columns-1:
			self.ix = self.app.thz_img.columns-1
			return False
		elif self.iy < 0:
			self.iy = 0
			return False
		elif self.iy > self.app.thz_img.rows-1:
			self.iy = self.app.thz_img.rows-1
			return False
		else:
			return True

	def set_coords(self, coords):
		self.ix, self.iy = coords

	def get_coords(self):
		return (self.ix, self.iy)

	def set_app_values(self):
		self.app.index_label.setText('Pixel Index: [{},{}]'.format(self.ix, self.iy))

	def paint_points(self):
		if self.app.options['points']:
			self.ax.scatter(self.ix, self.iy, edgecolors='w', color='r', alpha=1)
		if self.app.options['multiple_points']:
			for point in self.app.pixel_list:
				if self.app.options['transparent']:
					self.ax.scatter(point.ix, point.iy, edgecolors='w', facecolors='none', alpha=1)
				else:
					self.ax.scatter(point.ix, point.iy, edgecolors='w', color=point.color, alpha=1)
				self.ax.text(point.ix+1,point.iy+1, point.name,fontsize=10,color='w')

	def show_img(self, img, **kwargs):
		self.ax.clear()
		self.ax.imshow(img, **kwargs)
		self.paint_points()
		self.ax.set_axis_off()
		self.canvas.draw()
		self.canvas.flush_events()
		if self.app.options['axes']:
			self.cursor = Cursor(self.canvas.axes, useblit=False, 
				color='red', linewidth=0.75, linestyle='--')

	def animation(self, since, to, progress, **kwargs):
		frames = []
		prog = 0
		range_tuple = tuple(range(since, to))
		progress.setRange(prog, len(range_tuple))		
		for i in range_tuple:
			progress.setValue(prog)
			im = self.show_img(self.app.thz_img.get_img(i), animated=True, **kwargs)
			self.app.pulse_view.set_time_point_by_row(i, self.app.pulse)
			frames.append([im])
			time.sleep(0.00001)
			prog += 1
			if not self.app.animating:
				break

	def animated(self, since, to, progress, **kwargs):
		fig = plt.figure()
		ims = []
		for i in range(850, 900):
			img = self.app.thz_img.get_img(i)
			im = plt.imshow(img, **kwargs)
			ims.append([im])
		ani = animation.ArtistAnimation(fig, ims, interval=1, blit=True,repeat=True)
		writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
		ani.save("movie.mp4", writer=writer)
		# plt.show()