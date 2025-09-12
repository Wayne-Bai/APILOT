from PIL import Image

def evaluate_image_expression(image1, image2, operator):
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    if operator == '+':
        result = ImageChops.add(img1, img2)
    elif operator == '-':
        result = ImageChops.subtract(img1, img2)
    elif operator == '*':
        result = ImageChops.multiply(img1, img2)
    elif operator == '/':
        result = ImageChops.divide(img1, img2)
    else:
        raise ValueError("Invalid operator")

    result.save('result.png')

evaluate_image_expression('image1.png', 'image2.png', '+')
