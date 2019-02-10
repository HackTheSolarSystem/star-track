import os.path
import sys

from PIL import Image, ImageDraw, PILLOW_VERSION

if __name__ == '__main__':
	image = Image.open('download(8).png')
	width, height = image.size
		center = (int(0.5 * width), int(0.5 * height))
		yellow = (0, 0, 0, 255)
		ImageDraw.floodfill(image, xy=center, value=yellow)
		output_img = os.path.join('kmeans-filled.png')
		image.save(output_img)
