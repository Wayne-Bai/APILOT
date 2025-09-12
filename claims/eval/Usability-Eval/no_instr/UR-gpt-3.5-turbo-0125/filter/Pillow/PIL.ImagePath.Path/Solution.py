
from PIL import Image

# Create a new empty image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100))

# Save the image to a file
image.save('output.png')

# Show the image
image.show()
