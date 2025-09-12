from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
image = Image.new('RGB', (300, 200), color = (255, 255, 255))
draw = ImageDraw.Draw(image)

# Load a TrueType font
font = ImageFont.truetype("arial.ttf", 20)

# Set the color (black)
draw.text((10, 10), "Hello, Pillow!", font=font, fill=(0, 0, 0))

# Save the image
image.save("hello.png")
