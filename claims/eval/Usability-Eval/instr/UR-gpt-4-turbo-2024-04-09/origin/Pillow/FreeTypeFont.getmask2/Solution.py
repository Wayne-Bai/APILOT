from PIL import Image, ImageDraw, ImageFont

# Settings for the image
text = "Hello, World!"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 40
background_color = "white"
text_color = "black"

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Create an image
img = Image.new("RGB", (300, 100), background_color)
draw = ImageDraw.Draw(img)

# Calculate text size and position (centered)
text_width, text_height = draw.textsize(text, font=font)
text_x = (img.width - text_width) // 2
text_y = (img.height - text_height) // 2

# Draw the text
draw.text((text_x, text_y), text, font=font, fill=text_color)

# Save the image
img.save("text_bitmap.png")

# Optionally, show the image
img.show()
