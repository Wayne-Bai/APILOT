from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_img = img.convert("L")

    # Get the bounding box of non-zero regions
    bbox = grayscale_img.getbbox()

    return bbox

# Example usage
bounding_box = calculate_bounding_box('path_to_your_image.jpg')
print("Bounding box of non-zero regions:", bounding_box)
