from PIL import Image

# Open an image and convert it to grayscale
img = Image.open('input_image.jpg').convert('L')

# Create a palette of 16 colors
palette = img.getcolors(16)

# Map each pixel to its closest color in the palette
pal_img = img.quantize(palette=palette)

# Save the resulting image
pal_img.save('output_image.jpg')
