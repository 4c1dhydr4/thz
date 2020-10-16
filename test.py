import thz
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

file_path = 'D:\\THz\\Samples\\Arandano_01.csv'
thz_image = thz.THZImage(file_path)

fig = plt.figure()

ims = []
for i in range(800,1200):
	img = thz_image.get_img(i)
	# img = ndimage.gaussian_filter(img, 5)
	# sx = ndimage.sobel(img, axis=0, mode='constant')
	# sy = ndimage.sobel(img, axis=1, mode='constant')
	# sob = np.hypot(sx, sy)
	# im = plt.imshow(sob, interpolation='hanning')
	im = plt.imshow(img, interpolation='hanning', cmap='hot')
	# mask = img > img.mean()
	# label_im, nb_labels = ndimage.label(mask)
	# im = plt.imshow(label_im) 
	ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1, blit=True,
								repeat=True)


# FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
# ani.save('basic_animation.mp4', writer=FFwriter)
# ani.save('dynamic_images.mp4')

plt.show()