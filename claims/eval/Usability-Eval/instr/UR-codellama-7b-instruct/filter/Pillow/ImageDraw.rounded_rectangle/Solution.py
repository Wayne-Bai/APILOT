
from PIL import Image, ImageDraw, ImageFont

# Create a new image with the size of 300x200 and set the background color to white
img = Image.new('RGB', (300, 200), 'white')

# Draw a rounded rectangle on the image with the corners at (50, 50) with a radius of 50
draw = ImageDraw.Draw(img)
draw.rounded_rectangle((50, 50), (350, 150), 50, fill='black')

# Save the image to disk
img.save('rounded_rectangle.png')
