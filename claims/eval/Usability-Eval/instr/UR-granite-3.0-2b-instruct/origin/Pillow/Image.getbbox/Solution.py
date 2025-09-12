from PIL import Image

def calculate_bounding_box(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert('L')

    # Calculate the bounding box of non-zero regions
    bounding_box = image.getbbox()

    return bounding_box

# Test the function
image_path = 'path_to_your_image.jpg'
bounding_box = calculate_bounding_box(image_path)
print(f'Bounding box: {bounding_box}')
