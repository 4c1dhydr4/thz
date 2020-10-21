import thz
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
mpl.rcParams['animation.ffmpeg_path'] = r'C:\Dev\thz\animation\ffmpeg.exe'

file_path = 'D:\\THz\\Samples\\Arandano_01.csv'
thz_image = thz.THZImage(file_path)

"""
fig, (ax0, ax1) = plt.subplots(ncols=2, constrained_layout=True)

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

writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save("movie.avi", writer=writer)
# FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
# ani.save('basic_animation.mp4', writer=FFwriter)
# ani.save('dynamic_images.mp4')

plt.show()

"""

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 8))
ims = []
data = []
pulse = thz_image.get_column_index(13,20)
ax0.set_title('THz Image')
ax1.set_title('THz Pulse')

for i in range(800,1200):
	data.append(pulse[i])
	im1 = ax0.imshow(thz_image.get_img(i))
	im2, = ax1.plot(data, color='k')
	ims.append([im1, im2])

ani = animation.ArtistAnimation(fig, ims, interval=1, blit=True, repeat=False)

plt.show()