from PIL import Image, ImageChops, ImageEnhance

def evaluate_image_expression(image_path, expression):
    # Open the image file
    with Image.open(image_path) as img:
        # Example: assuming expression is to adjust brightness
        if expression.startswith("brightness"):
            factor = float(expression.split(":")[1])  # e.g., "brightness:1.5"
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(factor)
        # More image expressions can be handled here
        
        return img

# Example usage
output_image = evaluate_image_expression("path/to/image.jpg", "brightness:1.5")
output_image.show()  # Display the resulting image
