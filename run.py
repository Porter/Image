import os
for file in os.listdir("."):
	if file.endswith(".png"):
		os.system("python count.py out/" + file)
print count
