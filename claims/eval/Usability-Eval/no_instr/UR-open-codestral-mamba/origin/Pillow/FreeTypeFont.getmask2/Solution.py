from PIL import Image, ImageDraw, ImageFont

# Create a blank image object
image = Image.new("RGB", (500, 500), color=(255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Choose font type and size
font = ImageFont.truetype("arial.ttf", size=30)

# Position where the text will be placed
text_position = (175, 200)

# Text message
text = "Hello, World!"

# Color of the text
text_color = (0, 0, 0)

# Draw the text on the image
draw.text(text_position, text, font=font, fill=text_color)

# Save the image
image.save("text_bitmap.png")
