from PIL import Image, ImageChops

def evaluate_image_expression(image_path):
    """
    Loads an image, applies an example expression operation, and saves the result.
    Here, the example operation inverts the image colors (a common simple expression).
    
    Args:
        image_path (str): The path to the image file to be processed.
        
    Returns:
        None. The result is saved as 'output_image.png' directly.
    """
    # Load the image from the given path
    img = Image.open(image_path)
    
    # Example expression: Invert the image
    inverted_image = ImageChops.invert(img)
    
    # Save the output image
    inverted_image.save('output_image.png', 'PNG')

# Example use of the function
evaluate_image_expression('example.jpg')
