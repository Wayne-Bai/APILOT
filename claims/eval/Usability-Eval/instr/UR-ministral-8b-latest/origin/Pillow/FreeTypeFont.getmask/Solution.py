from PIL import ImageDraw, ImageFont

# Create a new image with a white background
width, height = 600, 400
background = (255, 255, 255)
image = Image.new('RGB', (width, height), background)

# Initialize a draw object
draw = ImageDraw.Draw(image)

# Specify the text and its properties
text = "Hello, World!"
font_size = 40
font_color = (0, 0, 0)
font = ImageFont.truetype("arial.ttf", font_size)

# Calculate the text size to position it correctly
text_width, text_height = draw.textsize(text, font=font)

x, y = (width - text_width) // 2, (height - text_height) // 2

# Draw the text on the image
draw.text((x, y), text, font=font, fill=font_color)

# Show the image
image.show()
