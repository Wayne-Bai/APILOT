from PIL import Image

def evaluate_image_expression(image_path, expression):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to RGB if it's not
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Get the image dimensions
    width, height = img.size

    # Evaluate the expression for each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the current pixel
            r, g, b = img.getpixel((x, y))

            # Evaluate the expression with the RGB values
            result = expression(r, g, b)

            # Print the result for the current pixel
            print(f"Pixel ({x}, {y}): ({r}, {g}, {b}) -> {result}")

# Example usage:
# Evaluate the expression f(r, g, b) = r + g + b
# for each pixel in the image at the path 'example.jpg'
evaluate_image_expression('example.jpg', lambda r, g, b: r + g + b)
