import subprocess
import os
 
print ("Hey this is Python Script Running\n")


tifs = [x for x in os.listdir('./output') if '.tif' in x]

def slice(files):


  # print(image_file)
  f = open("files.txt","w+")

  for file in files:
    f.write(file)
    f.write("\n")

  f.close()

  tmp = subprocess.call(["./reslice", "files.txt"]) 
  # os.remove("files.txt")

  # print ("printing result")
  print (tmp)

#end thats all

if __name__ == '__main__':
  # for t in tifs:
  slice(tifs)
