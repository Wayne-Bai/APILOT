
from PIL import ImageDraw

# Create a new image with a size of 500x500 pixels, with an alpha channel
image = Image.new('RGBA', (500, 500), (255, 255, 255))

# Create a Draw object to draw on the image
draw = ImageDraw.Draw(image)

# Define the rounded rectangle parameters
corner_radius = 10
rect_width = 300
rect_height = 200

# Calculate the coordinates of the top-left corner of the rectangle
x = (500 - rect_width) / 2
y = (500 - rect_height) / 2

# Define the rectangle coordinates
coords = ((x, y), (x + rect_width, y), (x + rect_width, y + rect_height), (x, y + rect_height))

# Draw the rounded rectangle
draw.roundrect(coords, corner_radius, fill='black')
