from PIL import Image, ImageDraw

# Define the parameters for the rounded rectangle
width, height = 300, 200
outer_radius = 50

# Create an image with a transparent background
image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw the rounded rectangle
draw.rectangle([
    (10, 10),  # left, top
    (width - 10, height - 10),  # right, bottom
], outline="black", fill=(128, 0, 0), radius=outer_radius)

# Show the image
image.show()
