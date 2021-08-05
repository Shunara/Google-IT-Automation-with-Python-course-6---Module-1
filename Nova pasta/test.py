#!/usr/bin/python3

# Import the libraries that will be used in this project
import os
from PIL import Image

def main():
	os.chdir("C:\\Users\\Leonardo\\Desktop\\Google-IT-Automation-with-Python-course-6---Module-1\\Nova pasta\\images")
	#print(os.listdir())
	files = os.listdir()
	i = 1
	for file in files:
		#print(file)
		im = Image.open(file)
		#os.chdir("C:\\Users\\Leonardo\\Desktop\\Google-IT-Automation-with-Python-course-6---Module-1\\Nova pasta - Copia")
		im.format = "JPG"
		#im.rotate(-90).resize((128,128))
		#os.chdir("C:\\Users\\Leonardo\\Desktop\\Google-IT-Automation-with-Python-course-6---Module-1\\Nova pasta - Copia")
		im.rotate(-90).resize((128,128)).save("C:\\Users\\Leonardo\\Desktop\\Google-IT-Automation-with-Python-course-6---Module-1\\Nova pasta - Copia\\"+
			"flipped_and_resized{}.jpg".format(i))
		print(im.format, im.size)
		i += 1

main()