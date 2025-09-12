from PIL import Image, ImageChops

def evaluate_image_expression(image_path, expression, target_image_path=None):
    # Open the input image
    image = Image.open(image_path)
    
    # Create a new image with the same size and mode as the input image
    output_image = Image.new(image.mode, image.size)
    
    # Iterate over each pixel
    for x in range(image.width):
        for y in range(image.height):
            # Get the pixel value at (x, y)
            pixel = image.getpixel((x, y))
            
            # Evaluate the expression for the current pixel
            evaluated_pixel = tuple(eval(expression) for v in pixel)
            
            # Put the evaluated pixel back in the output image
            output_image.putpixel((x, y), evaluated_pixel)
    
    # Save or show the evaluated image
    if target_image_path:
        output_image.save(target_image_path)
    else:
        output_image.show()

# Example usage:
# Assume you have an image named 'input.jpg'.
# The given expression here divides every pixel value by 2.
evaluate_image_expression('input.jpg', 'v // 2', 'evaluated_output.jpg')
