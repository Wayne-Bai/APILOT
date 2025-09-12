from PIL import Image

# Create a new 2D vector of pixel data of size 100x100 with RGB color mode
img = Image.new('RGB', (100, 100))

# Iterate over each pixel and set its color
for x in range(img.width):
    for y in range(img.height):
        img.putpixel((x, y), (x % 256, y % 256, 0))

# Save the image to a file
img.save('output.png')

# Display the image (optional)
img.show()
