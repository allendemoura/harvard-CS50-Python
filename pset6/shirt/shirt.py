from PIL import Image, ImageOps
import sys, os

if len(sys.argv) != 3:
    sys.exit("usage: shirt.py inputImage.jpg outputImage.jpg")
elif not sys.argv[1].lower().endswith((".jpg", ".png", ".jpeg")):
    sys.exit("CL args must be jpeg or png files")
elif os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
    sys.exit("CL args must be same file format")


try:
    # open shirt and define size
    shirt = Image.open("shirt.png")
    size = shirt.size
    # open input image and resize to fit shirt
    image = Image.open(sys.argv[1])
    image = ImageOps.fit(image, size)
    # paste shirt onto input image
    image.paste(shirt, shirt)
    # save new image in path given in CLA
    image.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File does not exist")

