from PIL import Image, ImageDraw

# Let's create a new image of size 200x200 pixels with a white background
image = Image.new('RGB', (200, 200), color=(255, 255, 255))

# Then, we will draw a rectangle on the image
# ImageDraw module provides shapes (line, rectangle, ellipse, etc.) and text drawing functions
draw = ImageDraw.Draw(image)
draw.rectangle([(50, 50), (150, 150)], fill=(0, 0, 255), outline=(0, 0, 0))

# At the end, we will save the image
image.save('output.png')
