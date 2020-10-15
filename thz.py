import csv
import numpy as np

class THZImage():
	dataset = [] #Numpy mxn
	file_path = ''
	filename = ''
	rows = 0.0
	columns = 0.0
	x_min = 0.0
	x_max = 0.0
	y_min = 0.0
	y_max = 0.0
	n_waveforms = 0
	pixels = []
	y_pixels = []
	x_pixels = []
	weights = tuple()
	dataset = []
	reference = []
	has_reference = False

	def __init__(self, path, progress=None):
		self.file_path = path
		self.load_dataset(progress)

	def load_dataset(self, progress=None):
		with open(self.file_path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line = 0
			if progress:
				progress.setRange(line, len([1 for row in csv_reader]))
				csv_file.seek(0)
			for row in csv_reader:
				if line == 0:
					self.filename = row[1]
				elif line == 1:
					self.rows = int(row[1])
				elif line == 2:
					self.columns = int(row[1])
					self.weights = (self.rows, self.columns)
				elif line == 3:
					self.x_min = float(row[1])
				elif line == 4:
					self.x_max = float(row[1])
				elif line == 5:
					self.y_min = float(row[1])
				elif line == 6:
					self.y_max = float(row[1])
				elif line == 8:
					self.pixels = np.array(list(map(int, row[1::])))
				elif line == 9:
					self.y_pixels = np.array(list(map(int, row[1::])))
				elif line == 10:
					self.x_pixels = np.array(list(map(int, row[1::])))
				elif line == 11:
					pass
				else:
					try:
						lrow = np.array(list(map(float, row[1::])))
					except:
						lrow = []
					# lrow = np.array([float(d) for d in row[1::] if d != ''])
					if len(lrow) != 0:
						self.reference.append(float(row[0]))
						self.dataset.append(lrow)
				line += 1
				if progress:
					progress.setValue(line)
			self.dataset = np.array(self.dataset)
			self.n_waveforms, self.n_pixels = self.dataset.shape
			self.reference = np.array(self.reference)
			if self.reference.sum() != 0:
				self.has_reference = True

	def get_row(self,row):
		return self.dataset[row, :]

	def get_column(self,column):
		return self.dataset[:, column]

	def get_column_index(self, x, y):
		for index in range(0, self.n_pixels):
			if x==self.x_pixels[index] and y==self.y_pixels[index]:
				return self.get_column(index)

	def get_img(self, row):
		return np.reshape(self.dataset[row,:], self.weights)

	def get_image_details(self):
		txt = 'Image Name: {}\n'.format(self.filename)
		txt += 'Reference Pulse: {}\n'.format('Yes' if self.has_reference else 'No')
		txt += 'Waveforms: {}\n'.format(self.n_waveforms)
		txt += 'Pixels (Total Pulses): {}\n'.format(self.n_pixels)
		txt += 'Image Rows: {}\n'.format(self.rows)
		txt += 'Image Columns: {}\n'.format(self.columns)
		txt += 'X Range:\n -Min: {}\n -Max:{}\n'.format(self.x_min, self.x_max)
		txt += 'Y Range:\n -Min: {}\n -Max:{}\n'.format(self.y_min, self.y_max)
		txt += 'File Path:\n {}\n'.format(self.file_path)
		return txt


class Pulse():
	data = None #Numpy mx1
	time_vector = None

	def __init__(self, data):
		self.data = data
		self.fft = np.abs(np.fft.fft(self.data))

	def set_time_vector(self, time_0, time_n):
		self.time_vector = np.linspace(time_0, time_n, data.shape[0])

	def get_frequency_domain(self, n):
		return self.fft[0:n], np.linspace(0,8,n)