# Importing necessary libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Loading the image using Pillow
def load_image(image_path):
    img = Image.open(image_path)
    return img

# Converting the image into a palette mapped image
def convert_to_palette_mapped_image(img):
    img = img.convert('RGB')
    img = img.convert('P', palette=Image.ADAPTIVE, colors=5)
    return img

# Generating color palette
def generate_color_palette(img):
    img = img.convert('RGB')
    img_array = np.array(img)
    img_array = img_array.reshape(-1, 3)
    palette = []
    for pixel in img_array:
        palette.append(tuple(pixel))
    counter = Counter(palette)
    color_palette = counter.most_common()
    return color_palette

# Displaying color palette
def display_color_palette(color_palette):
    colors = [color[0] for color in color_palette]
    counts = [color[1] for color in color_palette]
    plt.pie(counts, labels=colors, autopct='%1.1f%%')
    plt.title('Color Palette')
    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'  # replace with your image path
    img = load_image(image_path)
    img = convert_to_palette_mapped_image(img)
    color_palette = generate_color_palette(img)
    display_color_palette(color_palette)
