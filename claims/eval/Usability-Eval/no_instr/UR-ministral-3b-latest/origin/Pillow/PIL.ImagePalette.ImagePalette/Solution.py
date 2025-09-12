from PIL import Image

def generate_color_palette(image_path, n_colors=10):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode if it's not already in RGB
    image = image.convert('RGB')

    # Extract colors from the image
    colors = image.getdata()

    # Calculate the histogram of colors
    from collections import Counter
    color_counts = Counter(colors)

    # Get the most common colors
    sorted_colors = sorted(color_counts.items(), key=lambda item: item[1], reverse=True)
    top_colors = [color for color, _ in sorted_colors[:n_colors]]

    # Generate the palette as a hex list
    palette = [f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}' for color in top_colors]

    return palette

# Example usage
image_path = 'example.jpg'
palette = generate_color_palette(image_path, n_colors=10)
print(palette)
