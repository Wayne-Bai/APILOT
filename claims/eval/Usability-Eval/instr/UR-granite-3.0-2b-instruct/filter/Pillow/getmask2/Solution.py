from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (200, 50), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Choose a font
font = ImageFont.truetype('arial.ttf', 20)

# Choose a text and its position
text = "Hello, World!"
text_position = (10, 10)

# Draw the text on the image
draw.text(text_position, text, font=font, fill=(0, 0, 0))

# Save the image
img.save('text_bitmap.png')
