import glob
import shutil
import os

src_dir = "./labelled_images"

## create training validation destination set
try:
	os.makedirs("./train")
	os.makedirs("./valid")

except:
	## if the dir exists delet it and recreate
	shutil.rmtree("./train")
	shutil.rmtree("./valid")
	os.makedirs("./train")
	os.makedirs("./valid")

train_dir = "./train"
valid_dir = "./valid"

classes = ['Angiectasia', 'Erosion', 'Foreign body', 'Pylorus', 'Reduced mucosal view']


for class_name in classes:
	src_folder = src_dir + "/" + class_name
	train_folder = train_dir + "/" + class_name
	valid_folder = valid_dir + "/" + class_name
	## create training validation destination set
	try:
		os.makedirs(train_folder)
		os.makedirs(valid_folder)

	except:
		## if the dir exists delet it and recreate
		shutil.rmtree(train_folder)
		shutil.rmtree(valid_folder)
		os.makedirs(train_folder)
		os.makedirs(valid_folder)
	count = 0
	for jpgfile in glob.iglob(os.path.join(src_folder, "*.jpg")):

		if count == 200:
			break

		if count & 1:
			shutil.copy(jpgfile, train_folder)
		else:
			shutil.copy(jpgfile, valid_folder)
		count += 1

print("finished")