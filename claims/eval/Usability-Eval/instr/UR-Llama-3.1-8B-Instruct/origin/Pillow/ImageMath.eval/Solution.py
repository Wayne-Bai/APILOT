from PIL import Image, ImageEnhance

def evaluate_image_expression(image_path):
    """
    Evaluates an image expression by enhancing its contrast and brightness.

    Args:
    - image_path (str): The path to the image file.

    Returns:
    - enhanced_image (Image): The enhanced image.
    """
    
    # Open the image file using PIL
    image = Image.open(image_path)
    
    # Ensure the image is in RGB mode
    image = image.convert('RGB')
    
    # Create an ImageEnhance object to enhance the image
    enhancer = ImageEnhance.Contrast(image)
    
    # Enhance the image's contrast by a factor of 1.5
    enhanced_image = enhancer.enhance(1.5)
    
    # Use another enhancer to enhance the brightness of the image
    enhancer = ImageEnhance.Brightness(enhanced_image)
    enhanced_image = enhancer.enhance(1.5)
    
    return enhanced_image


# Example usage:
image_path = 'path_to_your_image.jpg'  # replace with your image file path
enhanced_image = evaluate_image_expression(image_path)

# Display the enhanced image
enhanced_image.show()
