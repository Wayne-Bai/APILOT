from PIL import Image

# Open the image file
img = Image.open('image.png')

# Create a palette
palette = [img.getpixel((x, y)) for x in range(img.width) for y in range(img.height)]

# Create a new image with the palette
new_img = Image.new('P', (img.width, img.height))
new_img.putpalette(palette)

# Save the new image
new_img.save('new_image.png')
