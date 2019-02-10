import subprocess
import os
 
print ("average Filtering ... \n")


tifs = [x for x in os.listdir('./processedStd') if '.tif' in x]

def denoise(image_file):

  print ("Processing File: " + image_file)
  tmp = subprocess.call(["./average", "50", image_file]) 

  # print (tmp)

#end thats all

if __name__ == '__main__':
  for t in tifs:
    denoise(t)

