
from PIL import Image, ImageDraw

# Create a new image with a size of 50x50 pixels
image = Image.new('RGB', (50, 50), (255, 255, 255))

# Create a drawing context for the image
drawing = ImageDraw.Draw(image)

# Draw a red line from (10, 10) to (40, 40)
drawing.line((10, 10), (40, 40), fill='red', width=5)

# Save the image to disk as a PNG file
image.save('output.png')
