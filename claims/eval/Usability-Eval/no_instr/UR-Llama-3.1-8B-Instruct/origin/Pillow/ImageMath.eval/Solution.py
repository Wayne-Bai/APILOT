# Import necessary libraries from Pillow
from PIL import Image, ImageChops

# Function to evaluate an image expression
def evaluate_image_expression(image_path, expression):
    """
    Evaluates an image expression.

    Args:
        image_path (str): The path to the image file.
        expression (str): The image expression to be evaluated.

    Returns:
        Image: The resulting image after applying the expression.
    """
    # Open the image file
    img = Image.open(image_path)

    # Apply the image expression
    if expression.lower() == "invert":
        # Invert the colors of the image
        result = ImageChops.invert(img)
    elif expression.lower() == "blur":
        # Blur the image using a Gaussian filter
        result = img.filter(ImageFilter.GaussianBlur(radius=5))
    elif expression.lower() == "edge detect":
        # Detect edges in the image
        result = img.filter(ImageFilter.FIND_EDGES)
    elif expression.lower() == "grayscale":
        # Convert the image to grayscale
        result = img.convert('L')
    elif expression.lower() == "resize to 50%":
        # Resize the image to 50% of its original size
        result = img.resize((img.width // 2, img.height // 2))
    elif expression.lower() == "resize to original":
        # Resize the image to its original size
        result = img.resize((img.width, img.height))
    else:
        # Default case: return the original image
        result = img

    return result

# Example usage:
image_path = "path_to_your_image.jpg"
expression = "invert"
result = evaluate_image_expression(image_path, expression)

# Display the result
result.show()
