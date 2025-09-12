from PIL import Image, ImageOps

def get_palette(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to RGB mode
    img = img.convert('RGB')

    # Get the palette
    palette = img.getpalette()

    return palette

# Usage
image_path = 'path_to_your_image.png'
palette = get_palette(image_path)
print(palette)
