from PIL import Image

def get_color_palette(image_path, num_colors):
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Resize image to reduce the number of pixels to process
    img = img.resize((150, 150))
    
    # Get the color palette
    img = img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    palette = img.getpalette()
    
    # Convert the palette to RGB values
    rgb_palette = []
    for i in range(0, len(palette), 3):
        rgb_palette.append((palette[i], palette[i+1], palette[i+2]))
    
    return rgb_palette

def print_color_palette(image_path, num_colors):
    color_palette = get_color_palette(image_path, num_colors)
    print(f"Color palette for the image {image_path}:")
    for i, color in enumerate(color_palette):
        print(f"Color {i+1}: RGB({color[0]}, {color[1]}, {color[2]})")

# Example usage:
image_path = 'image.jpg'
num_colors = 8
print_color_palette(image_path, num_colors)
