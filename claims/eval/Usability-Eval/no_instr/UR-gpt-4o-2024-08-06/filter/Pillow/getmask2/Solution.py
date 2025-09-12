from PIL import Image, ImageDraw, ImageFont

# Define image size and color
width, height = 200, 100
background_color = (255, 255, 255)
text_color = (0, 0, 0)

# Create a blank image with white background
image = Image.new('RGB', (width, height), color=background_color)

# Initialize the drawing context with the image object as background
draw = ImageDraw.Draw(image)

# Specify the font size and type (default to a basic font if specific fontfile isn't found)
try:
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

# Specify the text and position
text = "Hello, Bitmap!"
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

# Add the text to the image
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Save the image
image.save("text_bitmap.png")

# Open and display the image (optional)
image.show()
