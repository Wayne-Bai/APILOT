
from PIL import Image, ImageDraw

# Set the font and color
font = "Arial.ttf"
color = (0, 0, 0)

# Create the image
img = Image.new("RGB", (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Set the text and position
text = "Hello, world!"
x, y = 10, 10

# Draw the text
draw.text((x, y), text, font=font, fill=color)

# Save the image
img.save("hello_world.bmp")
