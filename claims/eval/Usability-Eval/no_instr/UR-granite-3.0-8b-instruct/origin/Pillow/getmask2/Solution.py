from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (200, 50), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.truetype('arial.ttf', 15)

# Draw the text on the image
draw.text((10, 10), 'Hello, World!', font=font, fill=(0, 0, 0))

# Save the image
img.save('hello_world.png')
