from PIL import Image
import os

name = raw_input('File name: ')
if name == '':
	name = 'out/20150907_193739.png'
image = Image.open(name)
rgb = image.convert('RGB')
w, h = image.size

copy = image.copy()
count = 0
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

print 'converting to list'
data = list(image.getdata())
print 'done'

x = 0
y = int(h*.1)

ox = x
oy = y

cookie = [156, 123, 80]

a = [[x, y]]
for i in range(1500):

	toLookAt = []
	for n in range(i):
		toLookAt.append([ox + n, oy + i])
	"""for n in range(i):
		toLookAt.append([ox + n, oy - i])"""
	for n in range(i):
		toLookAt.append([ox + i, oy + n])
	"""for n in range(i):
		toLookAt.append([ox - i, oy + n])"""

	print i, len(toLookAt)
	for n in toLookAt:
		colors =  data[n[0] + n[1]*w]
		diff = 0
		for j in range(3):
			diff += abs(cookie[j] - colors[j])
		if diff < 50:
			count += 1
			copy.putpixel((n[0], n[1]), (255, 0, 0))
		else:
			copy.putpixel((n[0], n[1]), (0, 0, 255))



print count
print float(count)/(w*h)
if not os.path.exists('./out/out'):
    os.makedirs('./out')
copy.save('out/' + name)
