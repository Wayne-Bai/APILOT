
from PIL import Image
import numpy as np

def color_palette(image):
    # Initialize a list to store the RGB values of the image pixels
    pixel_colors = []

    # Iterate through the pixels in the image
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # Get the RGB value of the current pixel
            r, g, b = image.getpixel((i, j))

            # If the color is not already in the palette, add it to the list
            if (r, g, b) not in pixel_colors:
                pixel_colors.append((r, g, b))

    # Return the palette as a dictionary of RGB values
    return {color: i for i, color in enumerate(pixel_colors)}
