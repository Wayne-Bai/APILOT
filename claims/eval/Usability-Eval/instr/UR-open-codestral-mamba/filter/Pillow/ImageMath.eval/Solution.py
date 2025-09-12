from PIL import Image
from PIL import ImageFilter

def evaluate_image_expression(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    gray_img = img.convert('L')

    # Apply the Unsharp Mask filter (edge detection)
    edge_img = gray_img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    # Display the original and filtered image
    img.show()
    edge_img.show()

# Use the path of your image
evaluate_image_expression('path_to_your_image.jpg')
