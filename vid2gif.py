#pip install MoviePy first


import os
from moviepy.editor import *

def convert():
	path = str(os.getcwd())
	resize = (int(input("Enter a size to resize to (percentage or width in pixels):\n")))
	factor = resize/100
	sizetype = ''

	for file in os.listdir("."):
		if file.endswith(".mp4") or file.endswith(".MP4") or file.endswith(".flv") or file.endswith(".avi") or file.endswith(".mkv"):
			vid = VideoFileClip(file)
			if resize > 100:
				vid = vid.resize(width=resize)
				sizetype =  str('px')
			else:
				vid = vid.resize(factor)
				sizetype = str('%')

			filename = str((file.split('.')[0]))
			vid.write_gif(filename + '_' + str(resize)+sizetype + '_.gif')


		print("Successfully converted file(s) to gif format")

if __name__=='__main__':
	convert()
