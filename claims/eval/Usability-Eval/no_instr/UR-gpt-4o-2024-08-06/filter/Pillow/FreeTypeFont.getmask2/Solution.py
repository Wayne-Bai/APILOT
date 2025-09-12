from PIL import Image, ImageDraw, ImageFont

# Define the size of the image
width, height = 200, 100

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text and font
text = "Hello, Bitmap!"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" # Modify this to the path to your font file
font_size = 20
font = ImageFont.truetype(font_path, font_size)

# Calculate the width and height of the text to be drawn
text_width, text_height = draw.textsize(text, font=font)

# Calculate X, Y position to center the text
x = (width - text_width) / 2
y = (height - text_height) / 2

# Add text to image
draw.text((x, y), text, font=font, fill='black')

# Save the image
image.save('text_bitmap.png')
