from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import csv
import sys
import os.path

def cleanup_coords(imarray):
	pixels_x = []
	pixels_y = []
	pixels = []

	# 1630
	y = imarray.shape[0]

	for i in imarray:
		x = 0
		for j in i:
			if j > 0:
				# 2 lines below are used to plot the cleaned up image
				#pixels_x.append(x)
				#pixels_y.append(y)

				pixels.append([x, y])
			x += 1
		y -= 1

	return pixels

def export_csv(centers, output):
	with open(output, mode='w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for i in centers:
			writer.writerow(i)


path = sys.argv[1]
for filename in os.listdir(path):
    csvout = "centroid_csv/" + filename + "-centroids.csv"
    if os.path.isfile(csvout):
        continue

    im = Image.open(path + '/' + filename)
    imarray = np.array(im)

    pixels = cleanup_coords(imarray)	

    try:
        kmeans = KMeans(n_clusters=50)
        kmeans.fit(pixels)
        y_kmeans = kmeans.predict(pixels)
        centers = kmeans.cluster_centers_

        export_csv(centers, csvout)
    except ValueError:
        continue

