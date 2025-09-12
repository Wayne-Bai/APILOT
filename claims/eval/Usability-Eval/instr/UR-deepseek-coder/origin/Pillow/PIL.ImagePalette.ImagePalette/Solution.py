from PIL import Image

def create_palette_mapped_image(image_path, palette_path, output_path):
    # Open the original image
    original_image = Image.open(image_path)
    
    # Open the palette image
    palette_image = Image.open(palette_path)
    
    # Ensure the palette image is in RGB mode
    if palette_image.mode != 'RGB':
        palette_image = palette_image.convert('RGB')
    
    # Extract the palette from the palette image
    palette = palette_image.getpalette()
    
    # Convert the original image to use the extracted palette
    palette_mapped_image = original_image.convert('P', palette=palette)
    
    # Save the palette-mapped image
    palette_mapped_image.save(output_path)

# Example usage
create_palette_mapped_image('input_image.png', 'palette_image.png', 'output_image.png')
