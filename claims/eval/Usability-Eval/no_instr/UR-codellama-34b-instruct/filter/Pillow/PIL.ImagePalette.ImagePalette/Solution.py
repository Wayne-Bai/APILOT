
from PIL import Image

# Load the image and get its palette
image = Image.open("image.png")
palette = image.getpalette()

# Create a new empty image with the same dimensions as the original image
new_image = Image.new(image.mode, image.size)

# Set the color palette for the new image
new_image.putpalette(palette)

# Save the new image to disk
new_image.save("new_image.png")
