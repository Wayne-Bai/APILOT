from PIL import Image, ImageDraw, ImageFont
# Create a new image
img = Image.new('RGB', (1000, 500), color='white')
# Create a drawing object
draw = ImageDraw.Draw(img)
# Load a font
font = ImageFont.truetype('arial.ttf', 20)
# Draw some text
draw.text((20, 20), 'Hello, world!', font=font, fill='black')
# Save the image
img.save('output.png')
