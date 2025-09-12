from PIL import Image

def calculate_bounding_box(image):
    # Convert the image to grayscale and then to binary
    grayscale_image = image.convert('L')
    binary_image = grayscale_image.point(lambda x: 0 if x == 0 else 255, '1')

    # Get the bounding box of the non-zero regions
    bbox = binary_image.getbbox()

    return bbox

# Example usage
image = Image.open('path_to_image.png')
bbox = calculate_bounding_box(image)
print(f"Bounding Box: {bbox}")
