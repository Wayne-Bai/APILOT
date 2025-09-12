
from PIL import Image, ImageChops

def evaluate_image_expression(image1_path, image2_path, operator):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    result = None
    if operator == "+":
        result = ImageChops.add(image1, image2)
    elif operator == "-":
        result = ImageChops.subtract(image1, image2)
    elif operator == "*":
        result = ImageChops.multiply(image1, image2)
    elif operator == "/":
        result = ImageChops.divide(image1, image2)
    
    if result:
        result.show()
    else:
        print("Invalid operator. Use one of the following: '+', '-', '*', '/'")

# Example usage
evaluate_image_expression("image1.jpg", "image2.jpg", "+")
