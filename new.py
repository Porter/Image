from PIL import Image
import os

name = raw_input('File name: ')
image = Image.open(name)
rgb = image.convert('RGB')
w, h = image.size

copy = Image.new('RGB', (w, h))
count = 0
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

print 'converting to list'
data = list(image.getdata())
print 'done'
for x in xrange(w):
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
  print str(x) + "/" + str(w)
  for y in xrange(h):
    r, g, b =  data[x + y*w]
    av = (r + g + b)/3.0
    if av > 255/2:
      count += 1
      copy.putpixel((x, y), (255, 0, 0))
    else:
      copy.putpixel((x, y), (r, g, b))
print count
print float(count)/(w*h)
if not os.path.exists('./out'):
    os.makedirs('./out')
copy.save('out/' + name)
