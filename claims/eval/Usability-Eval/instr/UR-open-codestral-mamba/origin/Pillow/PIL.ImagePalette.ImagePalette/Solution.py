# Importing the PIL module
from PIL import Image

# Open an image
img = Image.open('image.jpg')

# Convert the image to palette mode
img = img.convert('P', palette=Image.ADAPTIVE, colors=256)

# Get palette colors
palette = img.getpalette()

# Show the palette colors
for i in range(256):
    print(f'Color {i}: {palette[i*3:(i+1)*3]}')
