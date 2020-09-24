from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# from matplotlib.widgets import LassoSelector, Cursor
# from matplotlib.path import Path
# from matplotlib import patches as patches
# import random

plt.rcParams["figure.figsize"] = (20,10)
plt.rcParams["axes.grid"] = True

class ImgView(QWidget):
	
	def __init__(self, parent = None):

		QWidget.__init__(self, parent)
		self.fig = Figure(frameon=False)
		self.canvas = FigureCanvas(self.fig)
		vertical_layout = QVBoxLayout()
		vertical_layout.addWidget(self.canvas)
		self.canvas.axes = self.fig.add_axes([0, 0, 1, 1])
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.setLayout(vertical_layout)
		self.canvas.axes.clear()
		self.canvas.axes.set_axis_off()
		self.canvas.draw()
		self.layout().addWidget(self.toolbar)
	"""
	def onselect(self, verts):
		self.verts = verts_normalization(verts)
		path = Path(self.verts)
		self.tag_coords = get_central_point(self.verts)
		self.actual_color = get_rand_color()
		self.patch = patches.PathPatch(path, 
			facecolor=self.actual_color, lw=1,)
		self.patch.set_alpha(0.5)
		points = get_points(self.shape)
		self.grid = self.patch.contains_points(points, radius=1e-9)
		self.lasso_plane_list = get_pixel_list(self.grid)
		self.canvas.axes.add_patch(self.patch)
		self.fig.canvas.draw_idle()

	def paint_roi(self, roi):
		verts = verts_normalization(roi.verts)
		path = Path(verts)
		tag_coords = get_central_point(verts)
		actual_color = roi.color
		patch = patches.PathPatch(path, 
			facecolor=actual_color, lw=1,)
		patch.set_alpha(0.5)
		points = get_points(roi.shape)
		self.canvas.axes.add_patch(patch)
		self.fig.canvas.draw_idle()

	def select_lasso_area(self):
		self.lasso_plane_list = list()
		lasso_props = {'color':'red','linewidth':0.5,'alpha':1}
		self.lasso = LassoSelector(self.canvas.axes, self.onselect, lineprops=lasso_props)
		self.cursor = Cursor(self.canvas.axes, 
			useblit=False, color='red', linewidth=0.5)
		# plt.show()
	"""

	def clear_axes(self):
		self.canvas.axes.clear()
		self.canvas.draw()

	def show_img(self, img, **kwargs):
		self.canvas.axes.clear()
		self.canvas.axes.imshow(img, **kwargs)
		self.canvas.axes.set_axis_off()
		self.canvas.draw()
		self.canvas.show()