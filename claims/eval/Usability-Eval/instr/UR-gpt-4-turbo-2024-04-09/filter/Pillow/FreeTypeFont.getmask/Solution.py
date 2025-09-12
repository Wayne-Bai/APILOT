from PIL import Image, ImageDraw, ImageFont

# Define the text and font properties
text = "Hello, World!"
font_path = "arial.ttf"  # Update with the path to a .ttf file on your system
font_size = 40

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Create an image with white background
img = Image.new('RGB', (400, 100), color = (255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(img)

# Get the size of the text to be drawn
text_width, text_height = draw.textsize(text, font)

# Position the text
text_x = (400 - text_width) // 2
text_y = (100 - text_height) // 2

# Draw the text on the image
draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# Save the image
img.save('text_bitmap.png')

# Display the image (optional)
img.show()
