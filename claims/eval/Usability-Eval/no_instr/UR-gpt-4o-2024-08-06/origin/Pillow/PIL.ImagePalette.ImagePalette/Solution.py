from PIL import Image

# Open the image file
image = Image.open('palette_mapped_image.png')

# Get the palette information
palette = image.getpalette()

# Define the number of colors in the palette
num_colors = len(palette) // 3

# Create a new image to display the palette
palette_image = Image.new('RGB', (num_colors * 10, 10))

# Assign colors from the palette to the palette image
for i in range(num_colors):
    r, g, b = palette[i * 3:i * 3 + 3]
    for x in range(i * 10, (i + 1) * 10):
        for y in range(10):
            palette_image.putpixel((x, y), (r, g, b))

# Show the palette image
palette_image.show()
