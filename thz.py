import csv
import numpy as np

class THZImage():
	dataset = []
	file_path = ""
	rows = 0.0
	colums = 0.0
	x_min = 0.0
	x_max = 0.0
	y_min = 0.0
	y_max = 0.0
	pixels = 0.0
	y_pixels = 0.0
	x_pixels = 0.0
	weights = tuple()

	def __init__(self, path, progressBar=None):
		self.file_path = path
		self.load_dataset(progressBar)

	def load_dataset(self, progressBar=None):
		with open(self.file_path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			line = 0
			for row in csv_reader:
				if line == 0:
					self.filename = row[1]
				elif line == 1:
					self.rows = int(row[1])
				elif line == 2:
					self.colums = int(row[1])
					self.weights = (self.rows, self.colums)
				elif line == 3:
					self.x_min = float(row[1])
				elif line == 4:
					self.x_max = float(row[1])
				elif line == 5:
					self.y_min = float(row[1])
				elif line == 6:
					self.y_max = float(row[1])
				elif line == 8:
					self.pixels = np.array([int(x) for x in row[1::]])
				elif line == 9:
					self.y_pixels = np.array([int(x) for x in row[1::]])
				elif line == 10:
					self.x_pixels = np.array([int(x) for x in row[1::]])
				elif line == 11:
					pass
				else:
					step = 0
					lrow = np.array([float(d) for d in row[1::] if d != ''])
					if len(lrow) != 0:
						self.dataset.append(lrow)
				line += 1
			self.dataset = np.array(self.dataset)

	def get_row(self,row):
		return self.dataset[row, :]

	def get_column(self,column):
		return self.dataset[:, column]

	def get_img(self, row):
		return np.reshape(self.dataset[row,:],(self.rows, self.colums))