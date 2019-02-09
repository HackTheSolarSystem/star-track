from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Copy this file to the folder containing the tifs you want to convert

run from command line like this: python draw_folder.py


"""

tifs = [x for x in os.listdir('./') if '.tif' in x]

def make_binary_image(image_file):
    """
    image_file:
        (str), the location of the tif file

    outputs a  binarized image with points of interest highlighted
    """
    #Importing image
    im = Image.open(image_file)

    #converting image to numpy array
    imarray = np.array(im)

    #getting dimensions
    h, w = imarray.shape

    #shrinking output dimensions (remove later)
    h /= 10 ; w /= 10

    #creating threshold
    mn = imarray.mean() + 3 * imarray.std()

    #binarizing image
    tf = np.where(imarray > mn)

    #creating output image
    plt.figure(figsize=(w,h))
    plt.scatter(tf[1], -tf[0])
    nmsplit = image_file.split('.')
    plt.savefig(nmsplit[0] + 'bin.' + nmsplit[1])
    np.savetxt(nmsplit[0] + '.csv', tf, delimiter=",")

if __name__ == '__main__':
    for t in tifs:
        make_binary_image(t)
