
from PIL import Image

def generate_palette(image_path, num_colors):
    image = Image.open(image_path)
    image = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    image.show()

image_path = "input_image.jpg"
num_colors = 8
generate_palette(image_path, num_colors)
