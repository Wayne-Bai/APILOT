# Import necessary libraries
from PIL import Image

def calculate_bounding_box(image_path):
    """
    Calculates the bounding box of the non-zero regions in the image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        tuple: A tuple containing the bounding box coordinates (left, upper, right, lower) 
               or None if the image is empty.
    """

    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale and then to a boolean array
        # to easily identify non-zero regions
        boolean_array = img.convert('L') > 0

        # Get the bounding box coordinates
        left = 0
        upper = 0
        right = img.width - 1
        lower = img.height - 1

        # Iterate over the boolean array to find the bounding box
        for i in range(img.width):
            for j in range(img.height):
                if boolean_array.getpixel((i, j)):
                    left = i
                    break
            if left!= 0:
                break

        for i in range(img.height):
            for j in range(img.width):
                if boolean_array.getpixel((j, i)):
                    upper = i
                    break
            if upper!= 0:
                break

        for i in range(img.width - 1, -1, -1):
            for j in range(img.height):
                if boolean_array.getpixel((i, j)):
                    right = i
                    break
            if right!= img.width - 1:
                break

        for i in range(img.height - 1, -1, -1):
            for j in range(img.width):
                if boolean_array.getpixel((j, i)):
                    lower = i
                    break
            if lower!= img.height - 1:
                break

        # If the left is greater than the right, it means the image is empty
        if left > right:
            return None

        # Return the bounding box coordinates
        return (left, upper, right, lower)

# Example usage:
image_path = "path_to_your_image.jpg"
bounding_box = calculate_bounding_box(image_path)
if bounding_box:
    print(bounding_box)
else:
    print("The image is empty.")
