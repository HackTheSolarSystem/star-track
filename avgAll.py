import subprocess
import os
 
print ("Hey this is Python Script Running\n")


tifs = [x for x in os.listdir('./output') if '.tif' in x]

def denoise(image_file):

  tmp = subprocess.call(["./average", "50", image_file]) 

  print ("printing result")
  print (tmp)

#end thats all

if __name__ == '__main__':
  for t in tifs:
    denoise(t)

