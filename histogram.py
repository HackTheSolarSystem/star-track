# from PIL import Image
import numpy as np
import os
import cv2 as cv


tifs = [x for x in os.listdir('./comparedata') if '.tif' in x]

# outputs a list of "pixel # : frequency " values
# the data actually appears for pixel values that's a multiple of 5
def create_histogram(image_file):
    img = cv.imread('./comparedata/'+image_file, 1)

    rows, columns, channels = img.shape

    # blue_px = img[:,:,0]

    hist = cv.calcHist([img],[0],None,[256],[0,256])
    vals = range(0,255)

    # extracts values from a list of lists
    frequencies = [freq for px_val in hist for freq in px_val]
    # print(frequencies)
    
    for i in range(0,len(frequencies)):
        print(i, frequencies[i])

def threshold_blue(image_file, threshold):
    img = cv.imread('./comparedata/' + image_file, 1)
    rows, columns, channels = img.shape

    #new_img = np.zeros((rows, columns, 3))
    
    new_img = img.copy()

    for i in range(0, rows):
        for j in range (0, columns):
            blue_px_val = img.item(i,j,0)
            if blue_px_val <= threshold:
                new_img[i,j] = (0,0,0)
            # else:
                # new_img[i,j] = img[i,j]

    cv.imwrite('./output/'+ image_file, new_img)


if __name__ == '__main__':
    for t in tifs:
        print(t)
        threshold_blue(t, 75)
