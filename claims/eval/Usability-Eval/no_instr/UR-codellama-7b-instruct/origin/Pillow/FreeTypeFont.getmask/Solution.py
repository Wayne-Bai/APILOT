
from PIL import Image, ImageDraw, ImageFont

# Create an image object
image = Image.new('RGB', (100, 50), color=(255, 255, 255))

# Draw text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=24)
draw.text((10, 10), "Hello, World!", fill=(0, 0, 0), font=font)

# Save the image to a file
image.save('output.jpg')
