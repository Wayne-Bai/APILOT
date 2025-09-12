from PIL import Image, ImageDraw, ImageFont

# Define the text to be displayed
text = "Hello, World!"

# Create a blank image with a white background
image = Image.new('RGB', (200, 100), color = (255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Calculate the text size
text_size = draw.textsize(text, font=font)

# Calculate the position to center the text
position = ((image.width - text_size[0]) // 2, (image.height - text_size[1]) // 2)

# Draw the text on the image
draw.text(position, text, fill=(0, 0, 0), font=font)

# Save the image
image.save("text_bitmap.png")

# Optionally, show the image
image.show()
