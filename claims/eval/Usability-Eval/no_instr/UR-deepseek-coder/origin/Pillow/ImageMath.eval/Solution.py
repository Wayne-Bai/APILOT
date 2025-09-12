from PIL import Image, ImageFilter

def evaluate_image_expression(image_path, expression):
    # Open the image
    image = Image.open(image_path)

    # Apply the expression (example: blur the image)
    if expression == "blur":
        image = image.filter(ImageFilter.BLUR)
    elif expression == "sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif expression == "edge_enhance":
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif expression == "contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif expression == "detail":
        image = image.filter(ImageFilter.DETAIL)
    else:
        raise ValueError("Unsupported expression")

    # Save or display the modified image
    image.show()

# Example usage
evaluate_image_expression("input_image.jpg", "blur")
