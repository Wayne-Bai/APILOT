from PIL import Image, ImageDraw, ImageFont

# Define the text and font settings
text = "Hello, World!"
font_size = 40
font_path = "arial.ttf"  # Path to a TrueType font file

# Create a blank image with a white background
width, height = 400, 100
image = Image.new("RGB", (width, height), "white")

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Calculate the text size
text_width, text_height = draw.textsize(text, font=font)

# Calculate the position to center the text
x = (width - text_width) // 2
y = (height - text_height) // 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill="black")

# Save the image
image.save("text_bitmap.png")
