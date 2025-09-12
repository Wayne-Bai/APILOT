from PIL import Image, ImageDraw, ImageFont

def evaluate_image_expression(expression):
    # Assume the expression is a simple mathematical expression that can be represented as text in an image
    # Create an image with a specific size
    img = Image.new('RGB', (400, 300), color = (73, 109, 137))

    # Get a drawing context
    d = ImageDraw.Draw(img)

    # Specify a font
    font = ImageFont.truetype('arial.ttf', 45)

    # Draw the text
    d.text((10,10), expression, fill=(255, 255, 0), font=font)

    # Display the image (optional)
    img.show()

# Call the function
evaluate_image_expression("2 + 2 = 4")
