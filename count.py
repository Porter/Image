from PIL import Image
import os
import math
import sys

args = sys.argv
if len(args) > 1:
	name = args[1]
else:
	name = raw_input('File name: ')
if name == '':
	name = 'out/20150907_193739.png'
print "opening " + name
image = Image.open(name)
rgb = image.convert('RGB')
w, h = image.size

copy = image.copy()
count = 0
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def diff(col1, col2):
	return sum([abs(col1[i] - col2[i]) for i in range(len(col1))])


data = list(image.getdata())

count = 0
red = [255, 0, 0]

for x in range(w):
	print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
	print x
	for y in range(h):
		
		color = data[x + y*w]
		if diff(color, red) < 60:
			copy.putpixel((x, y), (0, 255, 0))
			count += 1
print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)



print count

if not os.path.exists('./out'):
	os.makedirs('./out')
if not os.path.exists('./out/out'):
	os.makedirs('./out/out')
print "saving..."
copy.save('out/' + name[:-3] + "png")
print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
