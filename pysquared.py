from __future__ import division
import sys
import os
from PIL import Image
def help():
    msg = "pysquared.py\n\n"
    msg = msg + "Usage: python pysquared <directory> <pixels>\n\n"
    msg = msg + "Example: pysquared ~/Desktop 128\n\n"
    msg = msg + "Will create a copy of all the '.jpg' files on the desktop, append the name '-squared' to the file name, crop to the largest sqaure and scale the image uniformally to <pixels>x<pixels> pixels.\n"
    return msg

if len(sys.argv) == 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print help()
    sys.exit("Program requires 2 arguments, ")

if len(sys.argv) < 3:
    print "Error: Two arguments expected. Use 'python pysquared --help' for more information."

directory = os.path.abspath(sys.argv[1])
if not os.path.exists(directory):
    print "Error: The path %s does not exist." % (directory)
jpegs = [x for x in os.listdir(directory) if x.endswith('.jpg')]
pixels = sys.argv[2]

"Processing:"
for file in jpegs:
    
    print "     file: ", file 
    img = Image.open(file)
    size = img.size
    print "     size:", size
    
    # What is the biggest square that can be made?
    W = size[0]
    H = size[1]
    crop = W if W >= H else H
    index = size.index(crop)
    if index == 0:
        # Width is maximum
        left = W/2 - H/2
        rect = (left, 0., left+H, H)
        img = img.crop(rect)
        
    else:
        # Height is maximum
        top = H/2 - W/2
        rect = (0., top, W, top+W)
        img = img.crop(rect)
    
    filename = file[0:len(file)-4] + "-squared.jpg"
    img = img.resize((int(pixels),int(pixels)), Image.ANTIALIAS)
    img.save(filename, "JPEG")
