
from PIL import Image, ImageDraw, ImageFont

# Define the font and font size
font = ImageFont.truetype('arial.ttf', 32)

# Create an empty image
width, height = (100, 50)
image = Image.new('RGB', (width, height), color='white')

# Get the drawing context
draw = ImageDraw.Draw(image)

# Draw the text on the image
text_w, text_h = draw.textsize("Hello, World!", font=font)
draw.text(((width - text_w) / 2, (height - text_h) / 2), "Hello, World!", font=font, fill='black')

# Save the image to a file
image.save('hello_world.bmp')
