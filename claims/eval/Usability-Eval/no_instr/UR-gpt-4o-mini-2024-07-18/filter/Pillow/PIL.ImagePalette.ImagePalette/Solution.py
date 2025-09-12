from PIL import Image, ImagePalette

def create_palette_image(color_list, image_size=(100, 100)):
    # Create a new image with palette mode
    palette_image = Image.new("P", image_size)

    # Create a new palette
    palette = ImagePalette.ImagePalette()

    # Add colors to the palette
    for color in color_list:
        palette.getcolor(color)

    # Assign the palette to the image
    palette_image.putpalette(palette)

    # Fill the image with the first color for demonstration
    for x in range(image_size[0]):
        for y in range(image_size[1]):
            palette_image.putpixel((x, y), 0)  # All pixels will use the first color in the palette

    return palette_image

# Example usage
color_list = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
palette_image = create_palette_image(color_list)
palette_image.show()
