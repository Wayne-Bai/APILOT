from PIL import Image, ImageDraw, ImageFont

# Define the size of the image
width, height = 200, 50

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text to be drawn
text = "Hello, World!"

# Choose a font and size
# You can specify a ttf file and size, e.g., using a default Pillow font
# font = ImageFont.truetype("arial.ttf", 20)
font = ImageFont.load_default()

# Calculate the size of the text to center it
textwidth, textheight = draw.textsize(text, font)
x = (width - textwidth) / 2
y = (height - textheight) / 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill='black')

# Save the image
image.save('text_bitmap.png')
