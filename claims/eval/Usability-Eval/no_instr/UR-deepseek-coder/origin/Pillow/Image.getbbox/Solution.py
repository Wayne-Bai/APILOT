from PIL import Image

def calculate_bounding_box(image):
    # Convert the image to grayscale and then to a binary image
    grayscale_image = image.convert('L')
    binary_image = grayscale_image.point(lambda p: p > 0 and 255)

    # Get the bounding box of the non-zero regions
    bbox = binary_image.getbbox()

    return bbox

# Example usage
if __name__ == "__main__":
    image = Image.open('path_to_image.jpg')
    bounding_box = calculate_bounding_box(image)
    print("Bounding Box:", bounding_box)
