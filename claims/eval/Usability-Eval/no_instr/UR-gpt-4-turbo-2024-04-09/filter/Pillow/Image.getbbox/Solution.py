from PIL import Image

def calculate_non_zero_bounding_box(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Convert image to grayscale
        img_gray = img.convert('L')

        # Get the bounding box
        bbox = img_gray.getbbox()
        return bbox

# Example usage:
image_path = 'path_to_your_image.jpg'
bounding_box = calculate_non_zero_bounding_box(image_path)
print("Bounding box of non-zero regions:", bounding_box)
