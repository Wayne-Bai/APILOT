from PIL import Image

def calculate_non_zero_bounding_box(image_path):
    image = Image.open(image_path)
    # Convert image to grayscale because bounding box is typically calculated on single channel
    gray_image = image.convert('L')
    # Find the bounding box of non-zero regions
    bbox = gray_image.getbbox()
    return bbox

# Example usage:
image_path = 'path_to_your_image.jpg'
bounding_box = calculate_non_zero_bounding_box(image_path)
print("Bounding box of non-zero regions:", bounding_box)
