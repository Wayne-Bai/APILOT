from PIL import Image, ImageDraw, ImageFont

# Create an image
image = Image.new('RGB', (500, 500), color='white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype("arial.ttf", 20)

# Draw text
draw.text((100, 100), "Hello World", font=font, fill='black')

# Save the image
image.save('hello_world.png')
