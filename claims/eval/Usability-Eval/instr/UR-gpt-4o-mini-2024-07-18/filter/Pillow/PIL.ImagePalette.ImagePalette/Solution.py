from PIL import Image, ImageDraw

def create_color_palette(colors, palette_width=200, palette_height=50):
    """
    Create a color palette image.

    :param colors: List of colors (as RGB tuples).
    :param palette_width: Width of the palette image.
    :param palette_height: Height of the palette image.
    :return: An Image object representing the color palette.
    """
    # Create a new image with a white background
    palette_image = Image.new('RGB', (palette_width, palette_height), 'white')
    draw = ImageDraw.Draw(palette_image)

    # Calculate the width for each color block
    block_width = palette_width // len(colors)

    # Draw the color blocks
    for i, color in enumerate(colors):
        draw.rectangle([i * block_width, 0, (i + 1) * block_width, palette_height], fill=color)

    return palette_image

# Example usage
if __name__ == "__main__":
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    palette = create_color_palette(colors)
    palette.show()  # Display the palette
