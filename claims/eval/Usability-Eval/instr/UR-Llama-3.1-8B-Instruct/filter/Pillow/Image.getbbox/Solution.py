# Import the necessary library
from PIL import Image
import numpy as np

def calculate_bounding_box(image_path):
    """
    This function calculates the bounding box of the non-zero regions in an image.

    Args:
    image_path (str): The path to the image file.

    Returns:
    tuple: A tuple containing the minimum x and y coordinates, and the width and height of the bounding box.
    """

    # Open the image using Pillow
    img = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Get the non-zero regions in the image
    non_zero_regions = np.argwhere(img_array!= 0)

    if non_zero_regions.size == 0:
        # If there are no non-zero regions, return a bounding box with coordinates (0, 0, 0, 0)
        return 0, 0, 0, 0

    # Get the minimum and maximum x and y coordinates of the non-zero regions
    min_x = np.min(non_zero_regions[:, 0])
    max_x = np.max(non_zero_regions[:, 0])
    min_y = np.min(non_zero_regions[:, 1])
    max_y = np.max(non_zero_regions[:, 1])

    # Calculate the width and height of the bounding box
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    return min_x, min_y, width, height

# Example usage
image_path = 'image.jpg'
min_x, min_y, width, height = calculate_bounding_box(image_path)
print(f"Bounded Box of Non-zero regions: [{min_x}, {min_y}], {width}x{height}")
