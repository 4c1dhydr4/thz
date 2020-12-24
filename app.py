from PyQt5 import (QtCore, QtGui, QtWidgets,)
from thz import (THZImage,Pulse,)
from components.combos import (fill_interpolation_cb, fill_cmaptype_cb, change_cmap_cb,
	fill_image_view_mode_cb,)
from components.progress import (set_progress,)
from components.tools import (show_message,)
from models.pixel import (save_pixel, refresh_pixels_tree, selected_pixels_tree, get_pixels_by_id)
from components.options import (set_checkboxes_options, set_pulse_plot_options,
	set_frequency_plot_options, set_transmittance_plot_options, set_absorbance_plot_options,)

class App(object):

	def _refresh(self):
		self.img_view.refresh()

	def _load_test(self):
		# self.file_path = 'D:\\THz\\Samples\\3.csv'
		self.file_path = 'D:\\THz\\Samples\\arandano_01.csv'
		self.progress = set_progress('Loading THz Image')
		self.thz_img = THZImage(self.file_path, self.progress)
		self.progress.close()
		self.on_load()

	def _imaging(self):
		if self.thz_img:
			cmap = str(self.cmap_cb.currentText())
			cmap = cmap if cmap != '' else None
			interpolation = str(self.interpolation_cb.currentText())
			self.img_view.show_img(
				self.thz_img.get_img(self.pulse_view.row),
				interpolation=interpolation,
				cmap=cmap)

	def _cmaptype(self):
		option = str(self.cmaptype_cb.currentText())
		change_cmap_cb(option, self.cmap_cb, self.first_load)
	
	def _key_press_event(self, event):
		key = event.key()
		if key == 65:
			self.img_view.ix -= 1
		elif key == 68:
			self.img_view.ix += 1
		elif key == 87:
			self.img_view.iy -= 1
		elif key == 83:
			self.img_view.iy += 1
		
		if self.img_view.control_coords():
			self._refresh()

	def _set_options(self, state):
		set_checkboxes_options(self)
		self._refresh()

	def _add_pixel_to_list(self):
		text, okPressed = QtWidgets.QInputDialog.getText(None, 
			"Pixel","Pixel Name:", QtWidgets.QLineEdit.Normal, "")
		if okPressed and text != '':
			save_pixel(self, text)
			self._refresh()

	def _remove_pixel_to_list(self):
		for id in selected_pixels_tree(self):
			pixel = get_pixels_by_id(self, id)
			self.pixel_list.remove(pixel)
		refresh_pixels_tree(self)
		self._refresh()

	def _change_color_pixel_list(self):
		for id in selected_pixels_tree(self):
			pixel = get_pixels_by_id(self, id)
			pixel.change_color()
		refresh_pixels_tree(self)
		# self._refresh()

	def _plot_pixels(self):
		self.pixels = selected_pixels_tree(self)
		self.pulse_plot.plot_pulses(self.pixels)
		self.frequency_plot.plot_freq(self.pixels)
		self.transmittance_plot.plot_transmittances(self.pixels)
		self.absorbance_plot.plot_absorbance(self.pixels)
		show_message('info', 
			'Pixel Analyze', 
			'Pixels loaded successful', 'Go to Analyze Tabs')

	def _pp_apply_changes(self):
		set_pulse_plot_options(self)
		self.pulse_plot.plot_pulses(selected_pixels_tree(self))
		self._refresh()

	def _fd_apply_changes(self):
		set_frequency_plot_options(self)
		self.frequency_plot.plot_freq(selected_pixels_tree(self))

	def _t_apply_changes(self):
		set_transmittance_plot_options(self)
		self.transmittance_plot.plot_transmittances(selected_pixels_tree(self))

	def _abs_apply_changes(self):
		set_absorbance_plot_options(self)
		self.absorbance_plot.plot_absorbance(selected_pixels_tree(self))

	def _stop_animation(self):
		self.animating = False

	def _animation_pulse(self):
		self._animation(pulse=True)

	def _animation(self, pulse=False):
		cmap = str(self.cmap_cb.currentText())
		cmap = cmap if cmap != '' else None
		interpolation = str(self.interpolation_cb.currentText())
		self.animating = True
		self.progress = set_progress('THz Animation by Time Point Progress')
		self.progress.canceled.connect(self._stop_animation)
		since = self.pulse_view.row
		if pulse:
			self.img_view.animation_pulsed(
				since, self.thz_img.n_waveforms, self.progress,
				interpolation=interpolation, cmap=cmap)
		else:
			self.img_view.animation(
				since, self.thz_img.n_waveforms, self.progress,
				interpolation=interpolation, cmap=cmap)
		self.progress.close()
		self._refresh()

	def _set_main_definitions(self, MainWindow):
		# Setear funciones a controles de interfaz con cada objeto (botones, sliders, etc.)
		self.first_load = True
		self.thz_img = None
		self.length = 300

		self.tab.setCurrentIndex(0)

		self.time_point_checkbox.setChecked(True)
		self.axes_checkbox.setChecked(True)
		self.point_checkbox.setChecked(True)
		self.multiple_points_checkbox.setChecked(True)
		self.transparent_checkbox.setChecked(True)
		self.grid_checkbox.setChecked(True)

		# Pulse Plot Tab
		self.time_start_line.setValidator(QtGui.QDoubleValidator(-30,30,3))
		self.time_end_line.setValidator(QtGui.QDoubleValidator(-30,30,3))
		self.pp_grid_checkbox.setChecked(True)
		self.pp_legend_checkbox.setChecked(True)
		self.pp_reload_button.clicked.connect(self._pp_apply_changes)

		#Frequency
		self.fd_grid_checkbox.setChecked(True)
		self.fd_legend_checkbox.setChecked(True)
		self.fd_reload_button.clicked.connect(self._fd_apply_changes)

		#Transmittance
		self.t_grid_checkbox.setChecked(True)
		self.t_legend_checkbox.setChecked(True)
		self.t_reload_button.clicked.connect(self._t_apply_changes)

		#Absorbance
		self.abs_grid_checkbox.setChecked(True)
		self.abs_legend_checkbox.setChecked(True)
		self.abs_reload_button.clicked.connect(self._abs_apply_changes)

		self.load_button.clicked.connect(self._load_test)
		self.cmaptype_cb.currentTextChanged.connect(self._cmaptype)
		self.cmap_cb.currentTextChanged.connect(self._imaging)
		self.interpolation_cb.currentTextChanged.connect(self._imaging)

		# Image Options
		self.time_point_checkbox.stateChanged.connect(self._set_options)
		self.axes_checkbox.stateChanged.connect(self._set_options)
		self.point_checkbox.stateChanged.connect(self._set_options)
		self.multiple_points_checkbox.stateChanged.connect(self._set_options)
		self.transparent_checkbox.stateChanged.connect(self._set_options)
		self.grid_checkbox.stateChanged.connect(self._set_options)

		self.animation_button.clicked.connect(self._animation)
		self.animation_pulse_button.clicked.connect(self._animation_pulse)
		self.add_pixel_button.clicked.connect(self._add_pixel_to_list)
		self.remove_pixel_button.clicked.connect(self._remove_pixel_to_list)
		self.change_color_button.clicked.connect(self._change_color_pixel_list)
		self.plot_pixels_button.clicked.connect(self._plot_pixels)

		fill_interpolation_cb(self.interpolation_cb)
		fill_cmaptype_cb(self.cmaptype_cb)
		fill_image_view_mode_cb(self.view_mode_cb)

		self.waveform_point_label.setText('Time Point: 0')
		self.index_label.setText('Pixel Index: [0,0]')
		self.sample_info_text.setReadOnly(True)

		MainWindow.keyPressEvent = self._key_press_event

		self.options = {
			'time_point': True,
			'axes': True,
			'points': True,
			'multiple_points': True,
			'transparent': True,
			'grid': True,
		}
		self.pp_options = {
			'grid':True,
			'legend':True,
			'reference':False,
		}
		self.fd_options = {
			'grid':True,
			'legend':True,
			'reference':False,
		}
		self.t_options = {
			'grid':True,
			'legend':True,
			'reference':False,
		}
		self.abs_options = {
			'grid':True,
			'legend':True,
		}
		self.plots_options = {
			'grid':True,
			'legend':True,
		}
		self.first_load = False

	def on_load(self):
		self.pixels_tree.clear()
		self.pixel_list = []
		self.pixel_num = 0
		self.img_view.app = self
		self.pulse_view.app = self
		self.plots_view.app = self
		self.pulse_plot.app = self
		self.frequency_plot.app = self
		self.transmittance_plot.app = self
		self.absorbance_plot.app = self
		self.pulse_view.onload()
		self.plots_view.onload()
		self.sample_info_text.setPlainText(self.thz_img.get_image_details())
		self.img_view.set_coords((int(self.thz_img.columns/2),int(self.thz_img.rows/2)))
		self.pulse = self.thz_img.get_column_index(*self.img_view.get_coords())
		self.pulse_view.refresh(self.pulse, onload=True)
		self.plots_view.refresh(self.pulse)
		self.img_view.set_app_values()