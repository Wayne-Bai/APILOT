from PIL import Image

def generate_palette(image_path, num_colors):
    image = Image.open(image_path)
    image.load()

    width, height = image.size
    palette = []

    for i in range(0, width, int(width / num_colors)):
        for j in range(0, height, int(height / num_colors)):
            pixel = image.getpixel((i, j))
            palette.append(pixel)

    palette = sorted(set(palette))

    return palette

# Example usage:
image_path = "path/to/your/image.jpg"
num_colors = 10
palette = generate_palette(image_path, num_colors)
print(palette)
