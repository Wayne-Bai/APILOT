
from PIL import Image, ImageFont, ImageDraw

# Set up the font and size
font = ImageFont.truetype("arial.ttf", 18)
text = "Hello World!"

# Create a new image with a transparent background
image = Image.new("RGB", (300, 50), (255, 255, 255))

# Draw the text on the image
draw = ImageDraw.Draw(image)
draw.text((10, 10), text, font=font)

# Save the image to a file
image.save("text_bitmap.bmp")
