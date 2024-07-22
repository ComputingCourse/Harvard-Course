import sys, PIL
from PIL import Image
import cv2
import numpy as np

#testing
if len(sys.argv) <3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-5:].lower() != ".jpeg" and sys.argv[1][-4:].lower() != ".jpg" and sys.argv[1][-4:].lower() != ".png":
    sys.exit("first file isnt of the right type")
elif sys.argv[1][-5:].lower() == ".jpeg" and sys.argv[2][-5:].lower() != ".jpeg":
    sys.exit("Input and output are not he same type")
elif sys.argv[1][-4:].lower() == ".jpg" and sys.argv[2][-4:].lower() != ".jpg":
    sys.exit("Input and output are not he same type")
elif sys.argv[1][-4:].lower() == ".png" and sys.argv[2][-4:].lower() != ".png":
    sys.exit("Input and output are not he same type")
try:
    file = open(sys.argv[1])
    file.close()
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


image1 = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")

image1 = PIL.ImageOps.fit(image1, (600,600))

image1.paste(shirt, mask=shirt)

image1.save(sys.argv[2])