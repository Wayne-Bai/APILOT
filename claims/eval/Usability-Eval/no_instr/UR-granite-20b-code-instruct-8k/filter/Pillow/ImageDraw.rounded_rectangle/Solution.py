
from PIL import Image, ImageDraw

# Create a blank canvas with a size of 300x200 pixels
canvas = Image.new('RGB', (300, 200))

# Create a drawing object
draw = ImageDraw.Draw(canvas)

# Draw a rounded rectangle with a radius of 20 pixels
draw.rectangle([50, 50, 250, 150], fill='blue', outline='red', width=2, rounded_corners=20)

# Save the image
canvas.save('rounded_rectangle.png')
