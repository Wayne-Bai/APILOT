from PIL import Image

def create_color_palette_image(colors):
    """
    Create an image with a palette showing the provided colors.
    
    Args:
    colors (list of tuples): A list where each tuple contains RGB values (Red, Green, Blue).

    Returns:
    Image: A PIL image object with the provided colors shown as a palette.
    """
    # Size of each color box
    box_size = 50
    # Create a new image with mode 'P' which stands for palette
    palette_image = Image.new("P", (box_size * len(colors), box_size))
    
    # Create a new palette with 256 colors (default palette size for mode 'P')
    # Setting all to black initially
    new_palette = [0] * 256 * 3
    
    # Fill the palette with the provided colors
    for i, color in enumerate(colors):
        new_palette[3 * i : 3 * i + 3] = color
    
    # Apply the custom colors to the image's palette
    palette_image.putpalette(new_palette)
    
    # Coloring the image blocks
    for i, color in enumerate(colors):
        for y in range(box_size):
            for x in range(i * box_size, (i + 1) * box_size):
                palette_image.putpixel((x, y), i)

    return palette_image

# Example usage:
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Red, Green, Blue, Yellow
palette_img = create_color_palette_image(colors)
palette_img.show()  # This will display the image
