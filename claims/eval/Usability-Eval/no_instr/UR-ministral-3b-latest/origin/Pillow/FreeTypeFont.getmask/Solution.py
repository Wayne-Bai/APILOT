from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
image = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(image)

# Load a font file (e.g., 'arial.ttf')
font = ImageFont.truetype('arial.ttf', 100)

# Define text and its position on the image
text = "Hello, World!"
position = (50, 50)

# Draw text on the image
draw.text(position, text, font=font, fill='black')

# Save the image
image.save('hello_world_bitmap.png')
