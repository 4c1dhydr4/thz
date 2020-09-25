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
	pixels = []
	y_pixels = []
	x_pixels = []
	weights = tuple()

	def __init__(self, path, progress=None):
		self.file_path = path
		self.load_dataset(progress)

	def load_dataset(self, progress=None):
		with open(self.file_path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			row_count = sum(1 for row in csv_reader)
			csv_file.seek(0)
			line = 0
			if progress:
				progress.setRange(line,row_count)
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
					lrow = np.array([float(d) for d in row[1::] if d != ''])
					if len(lrow) != 0:
						self.dataset.append(lrow)
				line += 1
				if progress:
					progress.setValue(line)
			self.dataset = np.array(self.dataset)

	def get_row(self,row):
		return self.dataset[row, :]

	def get_column(self,column):
		return self.dataset[:, column]

	def get_column_index(self, x, y):
		for index in range(0,len(self.x_pixels)):
			if x==self.x_pixels[index] and y==self.y_pixels[index]:
				return self.get_column(index)


	def get_img(self, row):
		return np.reshape(self.dataset[row,:], self.weights)