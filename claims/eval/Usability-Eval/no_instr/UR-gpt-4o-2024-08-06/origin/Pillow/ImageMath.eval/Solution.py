from PIL import Image, ImageChops

def evaluate_image_expression(image_path1, image_path2, operation, scale=1.0, offset=0):
    # Open the images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    
    # Ensure both images have the same mode and size
    if image1.mode != image2.mode or image1.size != image2.size:
        raise ValueError("Both images must have the same mode and size")
    
    # Perform the requested operation
    if operation == 'add':
        result_image = ImageChops.add(image1, image2, scale=scale, offset=offset)
    elif operation == 'subtract':
        result_image = ImageChops.subtract(image1, image2, scale=scale, offset=offset)
    elif operation == 'multiply':
        result_image = ImageChops.multiply(image1, image2)
    elif operation == 'difference':
        result_image = ImageChops.difference(image1, image2)
    else:
        raise ValueError("Unsupported operation. Use 'add', 'subtract', 'multiply', or 'difference'")
    
    return result_image

# Example usage:
# result = evaluate_image_expression("image1.jpg", "image2.jpg", "add")
# result.show()
