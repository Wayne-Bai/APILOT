from PIL import Image
import numpy as np

def calculate_bounding_box(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Convert the image to a numpy array
        image_array = np.array(image)

        # Calculate the bounding box of the non-zero regions
        x_min, x_max = np.min(image_array[:, :, 0]), np.max(image_array[:, :, 0])
        y_min, y_max = np.min(image_array[:, :, 1]), np.max(image_array[:, :, 1])
        z_min, z_max = np.min(image_array[:, :, 2]), np.max(image_array[:, :, 2])

        # Return the bounding box
        return (x_min, y_min, z_min), (x_max, y_max, z_max)
