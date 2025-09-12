from PIL import Image

def evaluate_image_expression(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Evaluate the image expression (e.g., calculate the average pixel value)
    expression_result = grayscale_image.getdata().mean()

    return expression_result
