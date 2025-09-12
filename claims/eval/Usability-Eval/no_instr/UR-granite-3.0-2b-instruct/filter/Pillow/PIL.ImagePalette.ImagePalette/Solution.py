from PIL import Image

def create_palette(image_path, num_colors):
    image = Image.open(image_path)
    image = image.convert('RGB')

    width, height = image.size
    palette = []

    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            if (r, g, b) not in palette:
                palette.append((r, g, b))
                if len(palette) == num_colors:
                    break
            else:
                continue
            break

    return palette

# Usage
image_path = 'path_to_your_image.png'
num_colors = 10
palette = create_palette(image_path, num_colors)
print(palette)
