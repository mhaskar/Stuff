#!/usr/bin/python

import os,time,sys

Directory = os.getcwd()
if os.path.isdir("results"):
	pass
else:
	os.mkdir("results")
file_name = []
for root,dirs,files in os.walk(Directory):
	for fn in files:
		if fn.endswith("mp4"):
			file_name.append(fn)


for mp4 in file_name:
	outputname = "{0}-480p-final.mp4".format(mp4.strip("mp4"))
	command = "ffmpeg -i '{0}' -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 results/'{1}'".format(mp4,outputname)
	os.system(command)
