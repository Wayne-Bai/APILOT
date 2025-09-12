
from PIL import Image

def calculate_bounding_box(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert image to grayscale

    non_zero_regions = image.point(lambda p: 255 if p > 0 else 0)

    bbox = non_zero_regions.getbbox()
    print("Bounding Box of Non-Zero Regions:", bbox)

# Example Usage
calculate_bounding_box('image.jpg')
