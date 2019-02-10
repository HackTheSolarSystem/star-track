import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from sklearn.linear_model import LinearRegression
import pandas as pd
import os
import cv2 as cv

"""
Copy this file to the folder containing the tifs you want to convert
run from command line like this: python draw_folder.py
"""

tifs = [x for x in os.listdir('./T152_Full') if '.tif' in x]

def make_binary_image(image_file):
    """
    image_file:
        (str), the location of the tif file
    outputs a  binarized image with points of interest highlighted
    """
    print('processing: ' + image_file)

    #Importing image
    imarray = cv.imread('./T152_Full/' + image_file,0)


    #getting dimensions
    h, w = imarray.shape

    #shrinking output dimensions (remove later)
    h /= 10 ; w /= 10

    #creating threshold
    mn = imarray.mean() + 3 * imarray.std()

    #binarizing image
    tf = np.where(imarray > mn)

    ret,thresh1 = cv.threshold(imarray,mn,255,cv.THRESH_BINARY)



    #creating output image
    print('writing: ' + image_file)

    cv.imwrite('./output/'+image_file, thresh1)



def outline_shape(csvfile):
    """
    csvfile:
        (str), the target csv file. csv file should have x and y coordinates and
        no header
    """

    df = pd.read_table(csvfile, header=None, delimiter=',')
    lr = LinearRegression()

    lr.fit(df[0].reshape(-1, 1), df[1].reshape(-1, 1))

    df[2] = [lr.predict(a) for a in df[0]]
    df[3] = df[1] > df[2]

    df = df.sort_values([3, 0])

    coords = []

    for i, r in df[df[3] == False].iterrows():
        coords.append([r[0], r[1]])

    for i, r in df[df[3] == True][::-1].iterrows():
        coords.append([r[0], r[1]])

    ring = LinearRing(coords)
    x, y = ring.xy

    fig = plt.figure(1, figsize=(15,15), dpi=90)
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    xrange = [0, 5000]
    yrange = [0, 1000]
    ax.set_xlim(*xrange)
    ax.set_ylim(*yrange)
    ax.set_aspect(1)
    plt.axis('off')

    nmsplt = csvfile.split('.')
    newname = nmsplt[-2] + '.jpg'

    plt.savefig(newname)

if __name__ == '__main__':
    for t in tifs:
        make_binary_image(t)
