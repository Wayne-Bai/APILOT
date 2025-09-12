from PIL import Image, ImageDraw, ImageFont

# Define the text
text = "Your Text Here"

# Define the font and size
font = ImageFont.truetype('arial.ttf', 40)  # replace 'arial.ttf' with your preferred font

# Get the size of the text
text_width, text_height = font.getsize(text)

# Create a new image with the correct size
img = Image.new('1', (text_width, text_height), 1)

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw the text on the image
draw.text((0, 0), text, font=font, fill=0)

# Save the image
img.save('text.bmp')
