import cv2
import numpy as np
import matplotlib.pyplot as plt

## create a filled image using cv2's dilation/erosion functions ##

def make_fill(input_img, output_img):
	img = cv2.imread(input_img,0)
	print(img)
	kernel = np.ones((100,100),np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	plt.imshow(closing)
	cv2.imwrite(output_img, closing)
