from PIL import Image

def calculate_bounding_box(image_path, output_image_path):
    # Open an image file
    image = Image.open(image_path)

    # Convert image to grayscale
    grayscale_image = image.convert('L')

    # Find the bounding box of the non-zero regions
    pixels = image.load()
    bounding_box = {
        'left': image.width,
        'top': image.height,
        'right': 0,
        'bottom': 0
    }

    for y in range(image.height):
        for x in range(image.width):
            if pixels[x, y] > 0:
                bounding_box['left'] = min(bounding_box['left'], x)
                bounding_box['top'] = min(bounding_box['top'], y)
                bounding_box['right'] = max(bounding_box['right'], x)
                bounding_box['bottom'] = max(bounding_box['bottom'], y)

    # Create the output image
    output_image = Image.new('RGBA', (bounding_box['right'] - bounding_box['left'] + 1, bounding_box['bottom'] - bounding_box['top'] + 1))
    for y in range(bounding_box['bottom'] - bounding_box['top'] + 1):
        for x in range(bounding_box['right'] - bounding_box['left'] + 1):
            output_image.putpixel((x, y), (0, 0, 0, 255))

    # Save the output image
    output_image.save(output_image_path)

# Example usage
image_path = 'path_to_input_image.jpg'
output_image_path = 'path_to_output_image.jpg'
calculate_bounding_box(image_path, output_image_path)
