# Importing the required libraries
from PIL import Image, ImageDraw

# Creating a new image with white background
image = Image.new('RGB', (400, 200), (255, 255, 255))
# Opening the created image
width, height = image.size
# Getting a drawing context
draw = ImageDraw.Draw(image)

# Function to draw a rounded rectangle
def draw_rounded_rectangle(draw, rectangle, radius):
    # Points to draw the rectangle
    x1, y1 = (rectangle[0], rectangle[1])
    x2, y2 = (rectangle[2], rectangle[3])

    # Coordinates for drawing the arc
    arc_coordinates = [
        (x1 + radius, y1),
        (x2 - radius, y1),
        (x2 - radius, y2),
        (x1 + radius, y2),
        (x1 + radius, y1),
    ]

    # Coordinates for the lines
    line_coordinates = [
        (arc_coordinates[0], arc_coordinates[3]),
        (arc_coordinates[4], arc_coordinates[1]),
        (arc_coordinates[2], arc_coordinates[5]),
        (arc_coordinates[0], arc_coordinates[5]),
    ]

    # Drawing the arcs
    draw.arc(arc_coordinates[0:4], 90, 270, fill=(0, 0, 0))
    draw.arc(arc_coordinates[4:8], 90, 270, fill=(0, 0, 0))

    # Drawing the lines
    draw.line(line_coordinates[0:4], fill=(0, 0, 0), width=2)

# Specifying the rounded rectangle's coordinates
rounded_rectangle = (50, 50, 350, 150)

# Defining the radius of the rounded corners
radius = 20

# Drawing the rounded rectangle on the image
draw_rounded_rectangle(draw, rounded_rectangle, radius)

# Saving the image
image.save('rounded_rectangle.png')
