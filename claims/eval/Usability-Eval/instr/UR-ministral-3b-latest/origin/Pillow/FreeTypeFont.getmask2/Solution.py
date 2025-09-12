from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
image = Image.new("RGB", (800, 200), "white")

# Initialize ImageDraw and set the color
draw = ImageDraw.Draw(image)
color = "black"

# Load the default font
font = ImageFont.load_default()

# Define the text
text = "Hello, world!"

# Calculate the position and size of the text
text_size = font.getsize(text)
pos = ((800-text_size[0])/2, (200-text_size[1])/2)

# Draw the text on the image
draw.text(pos, text, fill=color)

# Save or show the image
image.show()

# Alternatively, you can save the image
# image.save("image.png")
