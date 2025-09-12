from PIL import Image

def adjust_color_palette(image_path, output_path, color_palette):
    # Open the image file
    img = Image.open(image_path)

    # Convert the image to a PIL Image with the correct mode
    img = img.convert("RGB")

    # Define the new color palette
    new_palette = []
    for color in color_palette:
        r, g, b = color
        new_palette.append((r, g, b))

    # Replace the colors in the image with the new palette
    for i in range(3 * img.width * img.height):
        r, g, b = img.getpixel((int(i / (img.width * img.height) * img.width),
                                 int(i / (img.width * img.height) * img.height)))
        if (r, g, b) in new_palette:
            new_palette_index = new_palette.index((r, g, b))
            img.putpixel((i // (img.width * img.height) * img.width,
                          i // (3 * img.width) % img.width),
                         new_palette[new_palette_index])

    # Save the modified image
    img.save(output_path)

# Example usage:
color_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
adjust_color_palette('input_image.jpg', 'output_image.jpg', color_palette)
