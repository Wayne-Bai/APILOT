from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a white background
image = Image.new("RGB", (200, 100), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font file
font = ImageFont.truetype("arial.ttf", 36)

# Draw the text onto the image
draw.text((50, 50), "Hello, world!", font=font)

# Save the image
image.save("hello_world.bmp")
