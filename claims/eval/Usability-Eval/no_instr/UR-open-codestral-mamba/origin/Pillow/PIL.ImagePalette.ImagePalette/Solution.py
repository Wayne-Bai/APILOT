from PIL import Image

def image_color_palette(image_path, num_colors):
    # Open the image file
    img = Image.open(image_path)
    # Convert the image to RGB if it is not
    img = img.convert('RGB')

    # Resize the image to a small fixed size to reduce processing time
    img.thumbnail((100, 100))

    # Convert the image data to a flat list of pixels
    pixels = img.getdata()
    pixels = [pixel for pixel in pixels]

    # Use Python's built-in algorithms to find the dominant colors in the image
    colors, counts = zip(*img.quantize(num_colors).getcolors())

    # Sort the colors by count, so that the most common colors appear first
    ordered_colors = sorted(zip(counts, colors), reverse=True)[:num_colors]

    # Return the color palette
    return [rgb_to_hex(color) for count, color in ordered_colors]

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

# Replace 'image.jpg' with the path to your image file
color_palette = image_color_palette('image.jpg', 5)
print(color_palette)
