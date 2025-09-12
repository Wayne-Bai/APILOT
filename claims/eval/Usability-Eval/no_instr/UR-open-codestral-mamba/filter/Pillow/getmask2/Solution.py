from PIL import Image, ImageDraw, ImageFont

# Set the text
text = "Hello, World!"

# Set the size of the image
width, height = 300, 300

# Create an image and draw object
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Choose a default font size
font_size = 25
font = ImageFont.truetype("arial.ttf", font_size)

# Get the width and height of the text
text_width, text_height = draw.textsize(text, font)

# Calculate the offset for text centering
offset_x = (width - text_width) // 2
offset_y = (height - text_height) // 2

# Choose a color for the text (black)
text_color = (0, 0, 0)

# Draw the text
draw.text((offset_x, offset_y), text, text_color, font)

# Save the image
image.save("hello_world.png")
