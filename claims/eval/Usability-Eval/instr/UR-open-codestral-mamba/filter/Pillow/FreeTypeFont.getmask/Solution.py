from PIL import Image, ImageDraw, ImageFont

# Declare the dimensions of the image
img_width, img_height = 800, 600

# Create a blank image with specified dimensions
image = Image.new('RGB', (img_width, img_height), color='white')

# Get a drawing context on the image
draw = ImageDraw.Draw(image)

# Choose the text to be displayed and the font
text = "Hello World!"
font = ImageFont.truetype("arial.ttf", size=30)

# Add the text into the image
draw.text((50, 50), text, font=font, fill='Black')

# Display the image
image.show()
