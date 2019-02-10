import os, sys
import numpy as np
import cv2

'''This script creates a composite IMAGE from a directory full of images.
   In order to run this, you must pip install opencv-python (cv2):

   python stack_tifs.py INPUT_DIR output_file.png'''

# input_dir is the directory containing the tif files along the z axis
# output_file is the composite image of all of the tifs

def create_composite(input_dir, output_file):
    first_file = os.listdir(input_dir)[0]
    b1 = np.array(cv2.imread(os.path.join(input_dir, first_file)))
    for file in os.listdir(input_dir):
        b1 += np.array(cv2.imread(os.path.join(input_dir, file)))
    cv2.imwrite(output_file,b1)

if __name__ == "__main__":

    input_dir = sys.argv[1]
    output_file = sys.argv[2]

    create_composite(input_dir, output_file)
