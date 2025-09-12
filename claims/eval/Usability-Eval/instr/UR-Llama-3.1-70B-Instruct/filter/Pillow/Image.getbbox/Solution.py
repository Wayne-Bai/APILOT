# Import the required library
from PIL import Image

# Function to calculate the bounding box
def calculate_bounding_box(image_path):
    """
    Calculate the bounding box of the non-zero regions in the image.

    Args:
        image_path (str): Path to the input image.

    Returns:
        tuple: A 4-tuple defining the left, upper, right, and lower pixel coordinates.
    """
    # Open the image using Pillow
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        img_gray = img.convert('L')

        # Get the image's pixel data as a numpy array
        pixels = img_gray.load()

        # Initialize the bounding box coordinates
        left = img.width
        upper = img.height
        right = 0
        lower = 0

        # Iterate over the image's pixels
        for y in range(img.height):
            for x in range(img.width):
                # Get the pixel value
                pixel = pixels[x, y]

                # If the pixel is non-zero, update the bounding box
                if pixel!= 0:
                    left = min(left, x)
                    upper = min(upper, y)
                    right = max(right, x)
                    lower = max(lower, y)

    # Return the bounding box coordinates
    return (left, upper, right + 1, lower + 1)


# Example usage:
image_path = 'path_to_your_image.jpg'  # Replace with your image path
bounding_box = calculate_bounding_box(image_path)
print("Bounding Box:", bounding_box)
