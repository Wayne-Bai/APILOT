from PIL import Image

# Open the image file
image = Image.open("image.jpg")

# Reduce the image size to speed up processing
image = image.resize((100, 100))

# Get the image palette
palette = image.getpalette()

# Print the color values in the palette
print(palette)
