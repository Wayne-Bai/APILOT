from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (200, 100), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.truetype('arial.ttf', 36)

# Choose a color
text_color = (0, 0, 0)

# Choose the text
text = "Hello, World!"

# Draw the text on the image
draw.text((10, 10), text, font=font, fill=text_color)

# Save the image
img.save('text_image.png')
