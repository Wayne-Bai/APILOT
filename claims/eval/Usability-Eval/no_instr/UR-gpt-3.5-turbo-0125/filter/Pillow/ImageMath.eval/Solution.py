
from PIL import Image, ImageChops

def evaluate_image_expression(image_path1, image_path2, operator):
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    if operator == "+":
        result = ImageChops.add(img1, img2)
    elif operator == "-":
        result = ImageChops.subtract(img1, img2)
    elif operator == "*":
        result = ImageChops.multiply(img1, img2)
    elif operator == "/":
        result = ImageChops.blend(img1, img2, alpha=0.5)
    else:
        result = None

    return result

result_image = evaluate_image_expression("image1.jpg", "image2.jpg", "+")
result_image.show()
