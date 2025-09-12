# Import the necessary library (Pillow)
from PIL import Image, ImageDraw

# Create a new image with a size of 800x600 pixels
img = Image.new('RGB', (800, 600), (250, 250, 250))  # white background

# Create an ImageDraw object
draw = ImageDraw.Draw(img)

# Function to draw a rounded rectangle
def draw_rounded_rectangle(draw, x, y, width, height, radius, color):
    """
    Draw a rounded rectangle on the image.

    Parameters:
    draw (ImageDraw): ImageDraw object.
    x (int): x-coordinate of the top left corner of the rectangle.
    y (int): y-coordinate of the top left corner of the rectangle.
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
    radius (int): Radius of the rounded corners.
    color (tuple): Color of the rectangle.
    """
    draw.rectangle([(x, y), (x + width, y + radius)], fill=color)
    draw.rectangle([(x + width, y), (x + width - radius, y + height)], fill=color)
    draw.rectangle([(x + radius, y + height), (x + width, y + height)], fill=color)
    draw.rectangle([(x, y + height - radius), (x + width, y + height)], fill=color)
    draw.ellipse([(x, y + radius), (x + radius, y + radius)], fill=color)
    draw.ellipse([(x + width - radius, y + radius), (x + width, y + radius)], fill=color)
    draw.ellipse([(x + width - radius, y + height - radius), (x + width, y + height - radius)], fill=color)
    draw.ellipse([(x + radius, y + height - radius), (x + radius, y + height)], fill=color)

# Draw a rounded rectangle on the image with radius 10
draw_rounded_rectangle(draw, 100, 100, 200, 200, 10, (0, 0, 0))  # black color

# Display the image
img.show()
