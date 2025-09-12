from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (200, 50), color = (255, 255, 255))

# Create a draw object
d = ImageDraw.Draw(img)

# Choose a font
fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)

# Draw the text on the image
d.text((10, 10), 'Hello, World!', font=fnt, fill=(0, 0, 0))

# Save the image
img.save('text_image.png')
