
from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
width, height = 300, 100
image = Image.new('RGB', (width, height), 'white')

# Specify the text and font
text = "Sample Text"
font = ImageFont.load_default()

# Draw the text on the image
draw = ImageDraw.Draw(image)
text_width, text_height = draw.textsize(text, font)
x = (width - text_width) / 2
y = (height - text_height) / 2
draw.text((x, y), text, fill='black', font=font)

# Save the image
image.save('text_bitmap.png')
