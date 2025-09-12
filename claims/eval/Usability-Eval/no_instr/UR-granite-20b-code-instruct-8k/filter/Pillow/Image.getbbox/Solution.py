from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)
    
    # Convert the image to a binary image with non-zero regions
    binary_image = image.convert('L')
    
    # Calculate the bounding box of the non-zero regions
    bbox = binary_image.getbbox()
    
    return bbox
