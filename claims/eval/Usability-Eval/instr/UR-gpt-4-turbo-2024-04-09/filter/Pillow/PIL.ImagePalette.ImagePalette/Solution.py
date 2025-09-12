from PIL import Image

def create_color_palette(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to 'P' mode which stands for palette-based
        img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
        
        # Get the palette
        palette = img.getpalette()
        
        # Create a list to hold the RGB tuples
        color_palette = []
        
        # The palette has 768 elements (256 colors * 3(RGB))
        for i in range(0, len(palette), 3):
            rgb = (palette[i], palette[i+1], palette[i+2])
            color_palette.append(rgb)
        
        return color_palette

# Example usage:
image_path = 'path_to_your_image.jpg'
palette = create_color_palette(image_path)
print(palette)
