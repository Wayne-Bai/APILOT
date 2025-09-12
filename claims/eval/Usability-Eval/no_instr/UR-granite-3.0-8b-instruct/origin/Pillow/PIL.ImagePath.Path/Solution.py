from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
image = Image.new('RGB', (200, 200), color = (255, 255, 255))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.truetype('arial.ttf', 20)

# Define a vector
vector = (50, 50)

# Draw a line using the vector
draw.line([(0, 0), vector], fill=(0, 0, 0), width=2)

# Display the image
image.show()
