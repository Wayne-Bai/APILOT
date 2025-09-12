
from PIL import Image, ImageDraw, ImageFont

# Specify text content and font size
text = "Hello, Pillow!"
font_size = 36

# Choose a font style and create a font object
font = ImageFont.truetype("arial.ttf", font_size)

# Calculate text size to create a blank image
text_width, text_height = ImageDraw.Draw(Image.new('RGB', (1, 1))).textsize(text, font=font)

# Create a new blank image with calculated text size and desired background color
image = Image.new('RGB', (text_width, text_height), 'white')

# Get the drawing context on the image
draw = ImageDraw.Draw(image)

# Draw the text on the image
draw.text((0, 0), text, fill='black', font=font)

# Save or display the image
image.save('text_image.bmp')
