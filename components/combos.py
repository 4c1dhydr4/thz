
def fill_interpolation_cb(cb):
	options = ('none', 'nearest', 'bilinear', 'bicubic', 'spline16',
		'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
		'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos')
	cb.addItems(options)
	cb.setCurrentIndex(6) 

def fill_cmaptype_cb(cb):
	options = ('Perceptually Uniform Sequential',
		'Sequential','Sequential (2)',
		'Diverging','Cyclic', 'Qualitative', 
		'Miscellaneous')
	cb.addItems(options)

def change_cmap_cb(option, cb, first_load=False):
		cmaps = {
			'Perceptually Uniform Sequential': ('viridis', 'plasma', 'inferno', 'magma', 'cividis'),
			'Sequential': ('Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'),
			'Sequential (2)':('binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink','spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia','hot', 'afmhot', 'gist_heat', 'copper'),
			'Diverging': ('PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'),
			'Cyclic': ('twilight', 'twilight_shifted', 'hsv'),
			'Qualitative': ('Pastel1', 'Pastel2', 'Paired', 'Accent','Dark2', 'Set1', 'Set2', 'Set3','tab10', 'tab20', 'tab20b', 'tab20c'),
			'Miscellaneous':('flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern','gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg','gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar')
		}
		cb.clear()
		cb.addItems(cmaps[option])
		if first_load:
			cb.setCurrentIndex(2)


def fill_image_view_mode_cb(cb):
	option = (
		'Time Domain',
		'Frequency Domain',
		'Transmittance',
		'Absorbance',
	)
	cb.addItems(option)