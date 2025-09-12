# Import necessary modules
from PIL import Image

# Create a new 2D image with a size of 500x500 pixels and a mode 'RGB'
img = Image.new('RGB', (500, 500))

# Load a pixel access object to manipulate the image data
pixels = img.load()

# Iterate over each pixel and set the color to a gradient that changes from red (top) to blue (bottom)
for y in range(img.size[1]):
    for x in range(img.size[0]):
        # Calculate the color for the current pixel based on the position
        r = int(255 * (1 - y / img.size[1]))
        g = 0
        b = int(255 * y / img.size[1])
        
        # Assign the color to the pixel
        pixels[x, y] = (r, g, b)

# Save the image to a file
img.save('gradient_image.png')

# Open the saved image
img.show()
