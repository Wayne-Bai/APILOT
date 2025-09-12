from Pillow import Image
from collections import Counter

def get_color_palette(image_path, num_colors=10):
    img = Image.open(image_path)
    img = img.resize((150, 150))  # resize to make the process faster
    img = img.convert('RGB')
    pixels = img.getdata()
    pixel_counter = Counter(pixels)
    most_common = pixel_counter.most_common(num_colors)
    return [color for color, count in most_common]
