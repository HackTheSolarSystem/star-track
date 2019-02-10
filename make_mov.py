import os, sys
import numpy as np
import cv2

'''This script creates a composite MOVIE from a directory full of images.
   In order to run this, you must pip install opencv-python (cv2):

   python make_mov.py INPUT_DIR output_file.avi'''

# input_dir is the directory containing the tif files along the z axis
# output_file is the composite movie (avi format; can convert to .mov by opening in quicktime)
# credit: stackoverflow (https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python)

def create_movie(image_folder, video_name):

    images = [img for img in os.listdir(image_folder) if img.endswith(".tif")] # originally png
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

if __name__ == "__main__":

    input_dir = sys.argv[1]
    output_file = sys.argv[2]

    create_movie(input_dir, output_file)
