from PIL import Image, ImageFont, ImageDraw

# Set the font and size
font = ImageFont.truetype('arial.ttf', 24)

# Create a blank image for the text
image = Image.new('RGB', (500, 300), (255, 255, 255))

# Draw the text on the image
draw = ImageDraw.Draw(image)
draw.text((10, 10), 'Hello World!', fill=(0, 0, 0), font=font)

# Save the image to a file
image.save('hello_world.png')
