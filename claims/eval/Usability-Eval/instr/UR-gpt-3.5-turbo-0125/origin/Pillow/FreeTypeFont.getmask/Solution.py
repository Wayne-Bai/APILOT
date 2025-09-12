
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 400, 200
image = Image.new('RGB', (width, height), 'white')

# Load a font
font = ImageFont.load_default()

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Add text to the image
text = "Hello, Pillow!"
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) // 2
y = (height - text_height) // 2
draw.text((x, y), text, fill='black', font=font)

# Save the image
image.save('text_image.png')
