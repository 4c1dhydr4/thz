def set_checkboxes_options(self):
	if self.time_point_checkbox.isChecked():
		self.options['time_point'] = True
	else:
		self.options['time_point'] = False

	if self.axes_checkbox.isChecked():
		self.options['axes'] = True
	else:
		self.options['axes'] = False

	if self.point_checkbox.isChecked():
		self.options['points'] = True
	else:
		self.options['points'] = False

	if self.multiple_points_checkbox.isChecked():
		self.options['multiple_points'] = True
	else:
		self.options['multiple_points'] = False

	if self.transparent_checkbox.isChecked():
		self.options['transparent'] = True
	else:
		self.options['transparent'] = False

	if self.grid_checkbox.isChecked():
		self.options['grid'] = True
	else:
		self.options['grid'] = False

def set_pulse_plot_options(self):
	if self.pp_grid_checkbox.isChecked():
		self.pp_options['grid'] = True
	else:
		self.pp_options['grid'] = False

	if self.pp_legend_checkbox.isChecked():
		self.pp_options['legend'] = True
	else:
		self.pp_options['legend'] = False

	if self.pp_reference_checkbox.isChecked():
		self.pp_options['reference'] = True
	else:
		self.pp_options['reference'] = False

	try:
		time_0 = float(self.time_start_line.text())
		time_n = float(self.time_end_line.text())
		self.pulse_plot.set_time_vector(time_0, time_n)
	except:
		print("time range wrong")