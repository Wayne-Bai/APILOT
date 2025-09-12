
from PIL import Image

def calculate_bounding_box(image):
    # Get the size of the image
    width, height = image.size

    # Initialize a list to store the bounding box coordinates
    coords = []

    # Iterate through each pixel in the image and check if it is non-zero
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel != (0, 0, 0):
                # Add the coordinates of the non-zero pixel to the list
                coords.append((x, y))

    # Calculate the minimum and maximum x and y coordinates of the bounding box
    min_x = min(coords, key=lambda c: c[0])[0]
    max_x = max(coords, key=lambda c: c[0])[0]
    min_y = min(coords, key=lambda c: c[1])[1]
    max_y = max(coords, key=lambda c: c[1])[1]

    # Return the bounding box as a tuple of coordinates
    return (min_x, min_y, max_x - min_x, max_y - min_y)
