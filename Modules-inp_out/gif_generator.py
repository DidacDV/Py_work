from PIL import Image, ImageDraw
import sys
all_images = []

for arg in sys.argv[1:]:            #get all images from command-line
    all_images.append(arg)

image_l = [Image.open(file) for file in all_images]

try:
    image_l[0].save( 'result.gif', save_all=True, append_images=image_l[1:], loop=0)            #loop = 0 --> gif will loop forever
except IndexError:
    print("Insert at least 2 images")