from PIL import Image, ImageMath

def evaluate_image_expression(image1, image2, expression):
    # Open the images
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Evaluate the expression
    result = ImageMath.eval(expression, img1=img1, img2=img2)

    # Save the result
    result.save("output.png")

# Usage
evaluate_image_expression("image1.png", "image2.png", "img1 * 2 + img2")
