from PIL import Image, ImageOps

def bounding_box(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img = ImageOps.grayscale(img)

    # Get the bounding box
    box = img.getbbox()

    return box
