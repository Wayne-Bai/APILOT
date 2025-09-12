
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 400, 200
image = Image.new('RGB', (width, height), 'white')

# Load a font
font = ImageFont.truetype("arial.ttf", 36)

# Draw text on the image
draw = ImageDraw.Draw(image)
text = "Hello, Pillow!"
text_width, text_height = draw.textsize(text, font)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2
draw.text((text_x, text_y), text, fill='black', font=font)

image.show()
