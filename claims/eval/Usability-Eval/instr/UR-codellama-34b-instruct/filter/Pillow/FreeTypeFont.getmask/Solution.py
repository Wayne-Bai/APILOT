
from PIL import Image, ImageDraw, ImageFont

# Set the font and text
font = ImageFont.truetype("arial.ttf", 24)
text = "Hello World!"

# Create a new image with the correct size
width, height = font.getsize(text)
image = Image.new('RGB', (width, height), (255, 255, 255))

# Draw the text on the image
draw = ImageDraw.Draw(image)
draw.text((0, 0), text, font=font)

# Save the image to a file
image.save("hello_world.bmp")
