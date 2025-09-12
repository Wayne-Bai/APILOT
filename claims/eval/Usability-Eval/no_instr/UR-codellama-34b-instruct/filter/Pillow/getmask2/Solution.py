from PIL import Image, ImageDraw, ImageFont

# Load the font
font = ImageFont.truetype("arial.ttf", 12)

# Create a blank image with the correct size
img = Image.new('RGB', (400, 30), (255, 255, 255))

# Get a drawing context
draw = ImageDraw.Draw(img)

# Draw the text
draw.text((10, 10), "Hello World!", font=font, fill=(0, 0, 0))

# Save the image to disk
img.save("hello_world.bmp")
