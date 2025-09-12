from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (500, 500), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Define a font
font = ImageFont.truetype('arial.ttf', 30)

# Draw a text on the image
draw.text((100, 100), 'Hello, World!', font=font, fill=(0, 0, 0))

# Save the image
img.save('hello_world.png')
