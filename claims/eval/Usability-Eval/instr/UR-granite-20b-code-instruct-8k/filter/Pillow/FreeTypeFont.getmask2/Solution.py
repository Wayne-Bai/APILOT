from PIL import Image, ImageDraw, ImageFont

# Define the text and font
text = "Hello, World!"
font_size = 36
font = ImageFont.truetype("arial.ttf", font_size)

# Create a blank canvas
width, height = font.getsize(text)
image = Image.new("RGB", (width, height), color="white")

# Draw the text on the canvas
draw = ImageDraw.Draw(image)
draw.text((0, 0), text, font=font, fill="black")

# Save the image
image.save("hello_world.bmp")
