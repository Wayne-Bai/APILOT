from PIL import Image

def create_palette_image(filename):
    # Create a base image with a small size
    base_image = Image.new("P", (10, 10))
    
    # Define colors for the palette (R, G, B) tuples
    palette_colors = [
        (255, 0, 0),   # Red
        (0, 255, 0),   # Green
        (0, 0, 255),   # Blue
        (255, 255, 0), # Yellow
        (255, 165, 0), # Orange
        (128, 0, 128), # Purple
        (255, 192, 203),# Pink
        (192, 192, 192),# Silver
        (128, 128, 128),# Gray
        (0, 0, 0),     # Black
        (255, 255, 255) # White
    ]

    # Expand the palette to 256 colors, using our set colors
    palette = []
    for color in palette_colors:
        palette.extend(color)

    # Fill the rest of the palette with black
    palette.extend((0, 0, 0) * (256 - len(palette_colors)))
    
    # Set the image's palette
    base_image.putpalette(palette)

    # Save the image
    base_image.save(filename)

# Example usage:
create_palette_image("palette_mapped_image.png")
