from PIL import Image, ImageDraw, ImageFont

# Set the text and size
text = "Hello, World!"
size = (200, 200)

# Create a new image with a white background
img = Image.new('RGB', size, color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.truetype('arial.ttf', 36)

# Draw the text on the image
draw.text((10, 10), text, font=font, fill=(0, 0, 0))

# Save the image
img.save('text_bitmap.png')
