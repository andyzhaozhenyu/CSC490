from PIL import Image
import os





ImgLocation = "../data/"
CATEGORIES = {"Reduced mucosal view_2 GAN"}

# Create a list to store image paths
ImagePaths = []
for category in CATEGORIES:
	for image in list(os.listdir(ImgLocation + category)):
		ImagePaths = ImagePaths + [ImgLocation + category + "/" + image]
# print(ImagePaths)

# Load images
for img in ImagePaths:
	image = Image.open(img)
	region = image.crop((143, 58, 512, 426))
	name = img.split('/')[-1]
	# print(name)
	region.save(name)