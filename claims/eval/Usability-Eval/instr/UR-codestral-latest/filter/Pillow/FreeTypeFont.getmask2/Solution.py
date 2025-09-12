from PIL import Image, ImageDraw, ImageFont

# Set the text
text = "Hello, World!"

# Create a new image with a white background
img = Image.new('RGB', (300, 100), color=(255, 255, 255))

# Get a drawing object to write text onto the image
d = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.load_default()

# Draw the text
d.text((10, 50), text, fill=(0, 0, 0), font=font)

# Save the image
img.save('text_bitmap.bmp')
