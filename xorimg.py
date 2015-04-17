#!/usr/bin/python
from PIL import Image
import sys

if len(sys.argv) < 3:
    print 'Usage: xorimg.py <image 1> <image 2> <output image>'
    sys.exit()

img1 = sys.argv[1]
img2 = sys.argv[2]
out = sys.argv[3]

pic1 = Image.open(img1)
pic2 = Image.open(img2)
pic2 = pic2.resize(pic1.size)
newpic = Image.new('RGB', pic1.size)

for y in range(pic1.size[1]):
    for x in range(pic1.size[0]):
        pixel1 = pic1.getpixel((x, y))
        pixel2 = pic2.getpixel((x, y))
        newpixel = []
        for p in range(len(pixel1[:3])):
            newpixel.append(pixel1[p] ^ pixel2[p])
        newpixel = tuple(newpixel)
        newpic.putpixel((x, y), newpixel)

newpic.save(out)
