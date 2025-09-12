from PIL import Image

def calculate_bounding_box(image_path):
    # Open an image file
    with Image.open(image_path) as img:
        # Convert image to grayscale
        gray_img = img.convert('L')
        
        # Create a binary image where non-zero pixels are white and zero pixels are black
        binary_image = gray_img.point(lambda p: p > 0 and 255)
        
        # Get the bounding box of the non-zero regions
        bbox = binary_image.getbbox()
        
        return bbox

# Example usage
image_path = 'path_to_your_image.jpg'
bounding_box = calculate_bounding_box(image_path)
print("Bounding Box:", bounding_box)
