from PIL import Image
from collections import Counter

def color_palette(image_path, num_colors=10):
    img = Image.open(image_path)
    img = img.convert("RGB")

    # resize the image to reduce the number of pixels being scanned
    img.thumbnail((200, 200))

    # extract pixels
    pixels = list(img.getdata())

    # count the occurrences of each color
    counter = Counter(pixels)

    # find the most common colors
    common_colors = counter.most_common(num_colors)

    # return the colors without their counts
    return [color for color, count in common_colors]
