
from PIL import Image

def create_color_palette(image_path, num_colors):
    image = Image.open(image_path)
    
    # Convert image to palette mode with given number of colors
    palette_image = image.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    
    # Get the color palette from the palette image
    color_palette = palette_image.getpalette()
    
    print(color_palette)

# Example usage
create_color_palette('input_image.jpg', 10)
