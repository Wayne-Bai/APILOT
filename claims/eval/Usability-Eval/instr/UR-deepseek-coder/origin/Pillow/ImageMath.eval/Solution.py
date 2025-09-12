from PIL import Image, ImageFilter

def evaluate_image_expression(image_path, expression):
    # Open the image
    image = Image.open(image_path)

    # Apply the expression (example: applying a blur filter)
    if expression == "blur":
        processed_image = image.filter(ImageFilter.BLUR)
    elif expression == "sharpen":
        processed_image = image.filter(ImageFilter.SHARPEN)
    elif expression == "edge_enhance":
        processed_image = image.filter(ImageFilter.EDGE_ENHANCE)
    else:
        raise ValueError("Unsupported expression")

    # Save or display the processed image
    processed_image.show()

# Example usage
evaluate_image_expression("input_image.jpg", "blur")
