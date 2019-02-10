# from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
import os
import cv2 as cv

"""
Copy this file to the folder containing the tifs you want to convert

run from command line like this: python draw_folder.py


"""

tifs = [x for x in os.listdir('./processedBlue') if '.tif' in x]

def make_binary_image(image_file):
    """
    image_file:
        (str), the location of the tif file

    outputs a  binarized image with points of interest highlighted
    """
    print('processing: ' + image_file)

    #Importing image
    imarray = cv.imread('./processedBlue/' + image_file,0)


    #creating threshold
    mn = imarray.mean() + 3 * imarray.std()

    #binarizing image
    tf = np.where(imarray > mn)

    ret,thresh1 = cv.threshold(imarray,mn,255,cv.THRESH_BINARY)



    #creating output image
    # print('writing: ' + image_file)

    cv.imwrite('./processedStd/'+image_file, thresh1)


if __name__ == '__main__':
    for t in tifs:
        make_binary_image(t)
