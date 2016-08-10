#!/usr/bin/python

from PIL import Image
import sys

if len(sys.argv) != 3:
 print "usage : ./img_replace.py original_photo save_photo.png"
 sys.exit(0)
img = Image.open(sys.argv[1])
img = img.convert("RGB")
colors = img.getdata()

newcolor = []
for item in colors:
    if item[0] == 0 and item[1] == 255 and item[2] == 0:# item[0] = Red | item[1] = Green | item[2] = Blue
        newcolor.append((255, 255, 255)) # add the new RGB
    else:
        newcolor.append(item) 

img.putdata(newcolor)
img.save(sys.argv[2], "PNG")
