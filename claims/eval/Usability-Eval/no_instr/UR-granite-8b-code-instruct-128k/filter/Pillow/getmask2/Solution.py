from PIL import Image, ImageDraw, ImageFont
# Create a new image
img = Image.new("RGB", (256, 256), (255, 255, 255))
# Get a drawing context
draw = ImageDraw.Draw(img)
# Load a font
font = ImageFont.truetype("arial.ttf", 20)
# Draw text
draw.text((10, 10), "Hello, World!", font=font, fill=(0, 0, 0))
# Save the image
img.save("hello_world.bmp")
