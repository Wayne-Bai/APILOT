
from PIL import Image, ImageDraw, ImageFont

text = "Hello, World!"
font = ImageFont.load_default()  # Using default font

# Get the size of the text
text_width, text_height = font.getsize(text)

# Create a new image with white background and space for text
image = Image.new('RGB', (text_width, text_height), 'white')
draw = ImageDraw.Draw(image)

# Draw the text on the image
draw.text((0, 0), text, font=font, fill='black')

# Save the image
image.save('text_bitmap.png')
